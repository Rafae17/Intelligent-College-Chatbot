import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from Templates import template, bot_avatar, user_avatar
from langchain.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_avatar.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_avatar.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Intelligent College Assistant", page_icon=":books:")
    st.write(template, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Intelligent College Assistant ")
    user_question = st.text_input("Ask a question about MVSR:")
    if user_question:
        handle_userinput(user_question)

    pdf_file_path = "data\Faculty & Staff List.pdf"  # Specify the path or file name of the PDF file
    pdf_docs = [pdf_file_path]
                # get pdf text
    raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
    text_chunks = get_text_chunks(raw_text)

                # create vector store
    vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == '__main__':
    main()