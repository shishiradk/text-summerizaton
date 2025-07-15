import validators
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re

# Streamlit page config
st.set_page_config(page_title="OpenAI: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 OpenAI: Summarize Text From YT or Website")
st.subheader("Summarize from a YouTube video or Website URL")

# Sidebar: OpenAI API Key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", value="", type="password")

# URL input
generic_url = st.text_input("Enter a YouTube or Website URL", label_visibility="visible")

# Initialize LLM
llm = None
if openai_api_key:
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",  #  "gpt-4orgpt-3.5-turbo"
            temperature=0,
            openai_api_key=openai_api_key,
            max_tokens=1000
        )
    except Exception as e:
        st.error("Failed to initialize OpenAI LLM. Check your API key.")
        st.exception(e)

# Prompt template for summarization
prompt_template = """
Provide a concise summary (around 300 words) of the following content:

Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Extract YouTube transcript helper
def get_youtube_transcript(url):
    try:
        video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
        if not video_id_match:
            raise ValueError("Invalid YouTube URL format.")
        video_id = video_id_match.group(1)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item['text'] for item in transcript_list])
        return transcript_text
    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise Exception("No transcript found for this video.")
    except Exception as e:
        raise Exception(f"Failed to extract transcript: {e}")

# Main summarization logic
if st.button("Summarize the Content from YT or Website"):

    if not openai_api_key.strip() or not generic_url.strip():
        st.error("Please provide both the OpenAI API key and a valid URL.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL (e.g., a YouTube video or a website).")
    elif not llm:
        st.error("LLM is not initialized. Check your OpenAI API key.")
    else:
        try:
            with st.spinner("Fetching content and summarizing..."):

                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    transcript = get_youtube_transcript(generic_url)
                    from langchain.schema import Document
                    docs = [Document(page_content=transcript)]
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )
                    docs = loader.load()

                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)

                st.success("Summary:")
                st.write(output_summary)

        except Exception as e:
            st.error("An error occurred during summarization.")
            st.exception(e)
