import streamlit as st


def main():
    st.title('First Application')
    st.header('Data Visualization')
    st.markdown('Botão')
    
    button = st.button('Button')
    if button:
        st.markdown('Clicado')
    
    st.markdown('Check')
    check = st.checkbox('Checkbox')
    
    if check:
        st.markdown("Checked")
    
    st.markdown('Radio')
    radio = st.radio('Escolha uma das opções', ('1', '2'))
    
    if radio == '1':
        st.markdown('1')
    elif radio == '2':
        st.markdown('2')
    
    st.markdown('Select Box')
    select = st.selectbox('Escolha uma opção', ('1', '2'))
    
    if select == '1':
        st.markdown('1')
    elif select == '2':
        st.markdown('2')

    st.markdown('Multi Select')
    multi = st.multiselect('Escolha', ('1', '2'))
    
    if multi == '1':
        st.markdown('1')
    
    if multi == '2':
        st.markdown('2')

    st.markdown('File')
    file_uploader = st.file_uploader('Choose your file')

    if file_uploader is not None:
        st.markdown('File')

if __name__ == '__main__':
    main()