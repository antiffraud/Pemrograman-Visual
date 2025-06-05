class Styles:
    MAIN_WINDOW_STYLE = """
        QMainWindow {
            background-color: #f8f9fa;
        }
    """
    GENERAL_WIDGET_STYLE = """
        QWidget {
            background-color: #ffffff;
            color: #2c3e50;
        }
    """
    TAB_WIDGET_STYLE = """
        QTabWidget::pane {
            border: 1px solid #dee2e6;
            background-color: #ffffff;
        }
        QTabBar::tab {
            background-color: #e9ecef;
            color: #495057;
            padding: 8px 16px;
            margin-right: 2px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
        }
        QTabBar::tab:selected {
            background-color: #ffffff;
            color: #2c3e50;
            border-bottom: 2px solid #007bff;
        }
    """
    STUDENT_INFO_STATUS_STYLE = "font-weight: bold; color: #2c3e50; padding: 2px 10px;"
    STUDENT_INFO_CARD_STYLE = """
        QWidget {
            background-color: #e3f2fd;
            border: 1px solid #bbdefb;
            border-radius: 8px;
            margin: 10px; /* Outer margin for the card itself */
        }
    """

    STUDENT_NAME_LABEL_STYLE = "font-weight: bold; font-size: 14px; color: #1565c0; padding: 2px;"
    STUDENT_NIM_LABEL_STYLE = "font-size: 12px; color: #1976d2; padding: 2px;"

    FORM_WIDGET_STYLE = """
        QWidget {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            margin: 10px;
            padding: 15px;
        }
    """
    FORM_TITLE_STYLE = "font-weight: bold; font-size: 16px; color: #2c3e50; margin-bottom: 10px;"
    LINE_EDIT_STYLE = """
        QLineEdit {
            padding: 8px 12px;
            border: 2px solid #e9ecef;
            border-radius: 6px;
            font-size: 14px;
            background-color: #ffffff;
        }
        QLineEdit:focus {
            border-color: #007bff;
            outline: none;
        }
    """
    CLIPBOARD_LABEL_STYLE = "font-weight: bold; color: #6c757d;"
    CLIPBOARD_BUTTON_STYLE = """
        QPushButton {
            background-color: #6c757d;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 12px;
        }
        QPushButton:hover { background-color: #5a6268; }
        QPushButton:pressed { background-color: #495057; }
    """
    SAVE_BUTTON_STYLE = """
        QPushButton {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #218838;
        }
        QPushButton:pressed {
            background-color: #1e7e34;
        }
    """
    TABLE_CONTAINER_STYLE = """
        QWidget {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            margin: 10px;
        }
    """
    TABLE_TITLE_STYLE = "font-weight: bold; font-size: 16px; color: #2c3e50; margin-bottom: 10px;"
    TABLE_STYLE = """
        QTableWidget {
            gridline-color: #dee2e6;
            background-color: #ffffff;
            alternate-background-color: #f8f9fa;
            border: none;
        }
        QTableWidget::item {
            padding: 8px;
            border-bottom: 1px solid #dee2e6;
        }
        QTableWidget::item:selected {
            background-color: #007bff;
            color: white;
        }
        QTableWidget QHeaderView { 
            background-color: #e9ecef; 
        }
        QTableWidget QHeaderView::section { 
            background-color: #e9ecef;
            color: #495057;
            padding: 12px 10px; 
            border: 1px solid #dee2e6; 
            font-weight: bold;
            font-size: 13px;
            min-height: 40px; 
        }
        QTableWidget QHeaderView::section:hover {
            background-color: #dee2e6;
        }
        QTableWidget QHeaderView::section:pressed {
            background-color: #ced4da;
        }
    """

    DELETE_BUTTON_STYLE = """
        QPushButton {
            background-color: #dc3545;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 13px;
        }
        QPushButton:hover { background-color: #c82333; }
        QPushButton:pressed { background-color: #bd2130; }
    """
    EXPORT_BUTTON_STYLE = """
        QPushButton {
            background-color: #27ae60;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-weight: bold;
            font-size: 14px;
        }
        QPushButton:hover { background-color: #219a52; }
    """
    DOCK_WIDGET_STYLE = """
        QWidget {
            background-color: #f8f9fa;
            color: #2c3e50;
        }
    """
    DOCK_TITLE_STYLE = "font-weight: bold; font-size: 14px; color: #2c3e50; margin-bottom: 5px;"
    SEARCH_INPUT_STYLE = """
        QLineEdit {
            padding: 8px 12px;
            border: 2px solid #dee2e6;
            border-radius: 6px;
            font-size: 13px;
            background-color: #ffffff;
        }
        QLineEdit:focus { border-color: #007bff; }
    """
    CLEAR_SEARCH_BUTTON_STYLE = """
        QPushButton {
            background-color: #6c757d;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 12px;
        }
        QPushButton:hover { background-color: #5a6268; }
    """
    HELP_TEXT_EDIT_STYLE = """
        QTextEdit {
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 6px;
            padding: 10px;
        }
    """