import streamlit as st 
from langchain_core.prompts import PromptTemplate 
from langchain_community.llms import CTransformers 


# function to get a response from pre-built Llama 2 model 
def get_Llama_response(input_text, number_of_words, blog_style):

    ### Loading downloaded LLama2 model
    llm= CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {number_of_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'number_of_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,number_of_words=number_of_words))
    print(response)
    return response


# streamlit setting to host as webpage 

st.set_page_config(page_title="Blog Generation",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Blog Generation 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating two more columns for additonal 2 fields

col1,col2= st.columns([5,5])

with col1:
    number_of_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")


# final response  
if submit:
    st.write(get_Llama_response(input_text, number_of_words, blog_style))
