import streamlit as st

from rag_engine import ask_podcast_rag

st.set_page_config(page_title="Podcast RAG Chatbot", page_icon="🎙️")

st.title("🎙️ Podcast RAG Chatbot")
st.write("Ask questions about 'This American Life' podcast episodes!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response, docs, filter_used = ask_podcast_rag(prompt)

                st.markdown(response)

                # Optional: Show sources in an expander
                with st.expander("View Sources"):
                    if filter_used:
                        st.info(f"Filtered by: {filter_used}")
                    for i, doc in enumerate(docs):
                        st.markdown(
                            f"**Source {i + 1} (Episode {doc.metadata.get('episode')})**"
                        )
                        st.text(doc.page_content[:300] + "...")
                        st.divider()

                # Add assistant response to chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
