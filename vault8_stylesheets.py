button_style = '''
        QPushButton {
        border-radius: 25;
        font-weight: 700;
        color: #fff;
        border: 0.3rem solid transparent;
        background-color: #60605e;
        }
        QPushButton:hover {
        border-radius: 25;
        background-color: #787875;
        }
        QPushButton:pressed {
        border-radius: 25;
        color: #0F462D;
        background-color: #E4FFDF;
        }
        '''

form_style = '''
    QLineEdit {
    padding-left: 0.4em;
    border-radius: 12.5px;
    font-size: 5em;
    font-weight: 100;
}
'''

alert = "background-color: #ff4747; color: #ffffff;border: 0.1px; border-radius:16px;"
success = "background-color: #E4FFDF; color: #0F462D; border-radius:16px"

list_style = '''
        QListWidget{ 
        padding: 8px; 
        border : 2px solid transparent;
        border-radius: 20px; 
        background : #1B1D1C
        }
        QListWidget QScrollBar{
        background : lightblue
        }
        QListWidget::item{
        font-size: 20px;
        }
        QListView::item:selected{ 
        border-radius: 5px; 
        background : #E4FFDF;
        color: #0F462D;
}
'''
