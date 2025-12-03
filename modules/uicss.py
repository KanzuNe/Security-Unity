#Styling
def apply_login_styling(window):
    window.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
            color: white;
        }
        
        QLabel {
            color: white;
            font-weight: bold;
            font-size: 12px;
        }
        
        /* Style for main container/groupbox if you have one */
        QGroupBox {
            background-color: #2a2a2a;
            border: 2px solid #444444;
            border-radius: 8px;
            font-weight: bold;
            font-size: 14px;
            color: white;
            padding-top: 15px;
            margin-top: 10px;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 5px 15px 5px 15px;
            background-color: #444444;
            color: white;
            border-radius: 5px;
        }
        
        /* ComboBox styling */
        QComboBox {
            background-color: #2a2a2a;
            border: 2px solid white;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 12px;
            color: white;
            min-height: 20px;
        }
        
        QComboBox:focus {
            border-color: #3498db;
            background-color: #333333;
        }
        
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 25px;
            border-left: 1px solid white;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
            background-color: #444444;
        }
        
        QComboBox::down-arrow {
            image: none;
            border: 2px solid white;
            width: 6px;
            height: 6px;
            border-top: none;
            border-right: none;
            transform: rotate(-45deg);
        }
        
        QComboBox QAbstractItemView {
            background-color: #2a2a2a;
            border: 1px solid white;
            border-radius: 5px;
            selection-background-color: #3498db;
            selection-color: white;
            color: white;
        }
        
        /* Password field styling */
        QLineEdit {
            background-color: #2a2a2a;
            border: 2px solid white;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 12px;
            color: white;
            min-height: 20px;
        }
        
        QLineEdit:focus {
            border-color: #3498db;
            background-color: #333333;
        }
        
        QLineEdit[placeholderText] {
            color: #cccccc;
        }
        
        /* Button styling */
        QPushButton {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #4a90e2, stop: 1 #2471a3);
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px 30px;
            font-weight: bold;
            font-size: 13px;
            min-width: 120px;
        }
        
        QPushButton:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #5ba0f2, stop: 1 #3581b3);
        }
        
        QPushButton:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                              stop: 0 #2471a3, stop: 1 #1b4f72);
        }
        
        QPushButton:disabled {
            background-color: #666666;
            color: #999999;
        }
    """)

def apply_main_ui_styling(window):
    window.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
            color: white;
        }
        
        QLabel {
            color: white;
            font-weight: bold;
            font-size: 13px;
        }
        
        
        /* Search Section */
        QLineEdit {
            background-color: #2a2a2a;
            border: 2px solid white;
            border-radius: 6px;
            padding: 10px 15px;
            font-size: 13px;
            color: white;
            min-height: 10px;
        }
        
        QLineEdit:focus {
            border-color: #3498db;
            background-color: #333333;
        }
        
        QPushButton#SearchButton {
            background-color: #666666;
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            font-size: 13px;
            min-width: 80px;
            min-height: 25px;
        }
        
        QPushButton#SearchButton:hover {
            background-color: #777777;
        }
        
        /* Table Styling - Dark theme */
        QTableWidget {
            background-color: #2a2a2a;
            border: 2px solid #444444;
            border-radius: 8px;
            gridline-color: #444444;
            selection-background-color: #3498db;
            selection-color: white;
            font-size: 12px;
            alternate-background-color: #333333;
            color: white;
            outline: none;
        }
        
        QTableWidget::item {
            padding: 15px 10px;
            border-bottom: 1px solid #444444;
            border-right: 1px solid #444444;
            color: white;
            background-color: #2a2a2a;
            outline: none;
        }
        
        QTableWidget::item:selected {
            background-color: #3498db;
            color: white;
            border: none;
            outline: none;
        }
        
        QTableWidget::item:hover {
            background-color: #404040;
        }
        
        QTableWidget::item:focus {
            background-color: #3498db;
            color: white;
            border: none;
            outline: none;
        }
        
        /* Remove focus rectangle */
        QTableWidget:focus {
            outline: none;
        }
        
        QTableWidget::item:selected:focus {
            background-color: #3498db;
            color: white;
            border: none;
            outline: none;
        }
        
        QHeaderView::section {
            background-color: #444444;
            color: white;
            padding: 15px 10px;
            border: none;
            font-weight: bold;
            font-size: 13px;
        }
        
        QHeaderView::section:horizontal {
            border-right: 1px solid #666666;
        }
        
        QHeaderView::section:vertical {
            background-color: #444444;
            color: white;
            padding: 15px 10px;
            border: none;
            font-weight: bold;
            font-size: 13px;
            border-bottom: 1px solid #666666;
        }
        

        QTableWidget QTableCornerButton::section {
            background-color: #444444;
            border: none;
        }
        
        /* Action Buttons */
        QPushButton {
            background-color: #555555;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 8px;
            min-width: 100px;
            min-height: 35px;
            margin: 5px;
        }
        
        QPushButton:hover {
            background-color: #666666;
        }
        
        QPushButton:pressed {
            background-color: #444444;
        }
        
        /* Colored Action Buttons */
        QPushButton#AddNew {
            background-color: #27ae60;
            font-size: 14px;
        }
        
        QPushButton#AddNew:hover {
            background-color: #2ecc71;
        }
        
        QPushButton#Update {
            background-color: #f39c12;
            font-size: 14px;
        }
        
        QPushButton#Update:hover {
            background-color: #e67e22;
        }
        
        QPushButton#Delete {
            background-color: #e74c3c;
            font-size: 14px;
        }
        
        QPushButton#Delete:hover {
            background-color: #c0392b;
        }
        
        QPushButton#GenerateRan {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #4a90e2, stop: 1 #2471a3);
            font-size: 14px;
        }
        
        QPushButton#GenerateRan:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0 #5ba0f2, stop: 1 #3581b3);
        }
        
        /* Password Strength Section */
        QProgressBar {
            border: 2px solid #444444;
            border-radius: 8px;
            text-align: center;
            background-color: #2a2a2a;
            font-weight: bold;
            font-size: 12px;
            min-height: 25px;
            max-height: 25px;
            color: white;
        }
        
        QProgressBar::chunk {
            border-radius: 6px;
            margin: 2px;
        }
        
        /* Status Label */
        QLabel#status {
            font-size: 13px;
            font-weight: bold;
            padding: 8px;
            color: white;
        }
        
        /* Groupbox styling if present */
        QGroupBox {
            background-color: #2a2a2a;
            border: 2px solid #444444;
            border-radius: 10px;
            font-weight: bold;
            font-size: 15px;
            color: white;
        }
        
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 15px;
            background-color: #444444;
            color: white;
            border-radius: 6px;
            font-size: 14px;
            padding: 8px 20px;
        }
    """)


def apply_popup_styling(window):
    window.setStyleSheet("""
        QMainWindow {
            background-color: #1e1e1e;
            color: white;
        }
        
        QWidget {
            background-color: #1e1e1e;
            color: white;
        }
        
        QLabel {
            color: white;
            font-weight: bold;
            font-size: 14px;
            padding: 8px;
            background-color: transparent;
        }
        
        
        QLineEdit {
            background-color: #1e1e1e;
            border: 2px solid white;
            border-radius: 4px;
            font-size: 14px;
            color: white;
            min-height: 30px;
            margin: 5px;
        }
        
        QLineEdit:focus {
            border-color: #3498db;
            background-color: #2a2a2a;
        }
        
        QLineEdit:hover {
            background-color: #2a2a2a;
        }
        
        /* Buttons */
        QPushButton {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #4a90e2, stop: 1 #2471a3);
            color: white;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            font-size: 14px;
            min-width: 150px;
            min-height: 45px;
            margin: 15px;
        }
        
        QPushButton:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #5ba0f2, stop: 1 #3581b3);
        }
        
        QPushButton:pressed {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #2471a3, stop: 1 #1b4f72);
        }
        
        /* Form Container */
        QGroupBox {
            background-color: #1e1e1e;
            border: none;
            color: white;
            font-weight: bold;
            font-size: 16px;
            padding-top: 20px;
            margin: 10px;
        }
        
        QGroupBox::title {
            color: white;
            padding: 5px;
            font-size: 16px;
        }
        
        QDialog {
            background-color: #1e1e1e;
            color: white;
        }
        
        QMessageBox {
            background-color: #1e1e1e;
            color: black;
        }
        
        QMessageBox QLabel {
            color: black;
            background-color: white;
            padding: 10px;
        }
        
        QMessageBox QPushButton {
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: bold;
        }
    """)