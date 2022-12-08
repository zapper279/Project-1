from math import pi as pi
from PyQt5.QtWidgets import *
from gui import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    '''Just a function that sets up for the gui'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def square_area(self):
        '''
        A function that takes the input of the user and returns the area of a square
        :return: the area of a square using input from the user
        '''
        self.side = float(self.side_input.text()) #Any positive int or float value
        self.s_area = self.side ** 2
        return self.s_area

    def triangle_area(self):
        '''
        A function that takes the input of the user and returns the area of a triangle
        :return: the area of a triangle using input from the user
        '''
        self.side1 = float(self.side1_input.text()) #Any positive int or float value
        self.side2 = float(self.side2_input.text()) #Any positive int or float value
        self.t_area = (self.side1 * self.side2) / 2
        return self.t_area

    def rectangle_area(self):
        '''
        A function that takes the input of the user and returns the area of a rectangle
        :return: the area of a rectangle using input from the user
        '''
        self.width = float(self.width_input.text()) #Any positive int or float value
        self.length = float(self.length_input.text()) #Any positive int or float value
        self.r_area = self.width * self.length
        return self.r_area

    def circle_area(self):
        '''
        A function that takes the input of the user and returns the area  of a circle
        :return: the area of a circle using input from the user
        '''
        self.radius = float(self.radius_input.text()) #Any positive int or float value
        self.c_area = pi * (self.radius ** 2)
        return self.c_area, 2

    def square_perimeter(self):
        '''
        A function that takes the input of the user and returns the perimeter of a square
        :return: the perimeter of a square using input from the user
        '''
        self.side = float(self.side_input.text()) #Any positive int or float value
        self.s_perimeter = self.side * 4
        return self.s_perimeter

    def triangle_perimeter(self):
        '''
        A function that takes the input of the user and returns the perimeter of a triangle
        :return: the perimeter of a triangle using input from the user
        '''
        self.side1 = float(self.side1_input.text()) #Any positive int or float value
        self.side2 = float(self.side2_input.text()) #Any positive int or float value
        self.side3 = float(self.side3_input.text()) #Any positive int or float value
        self.t_perimeter = self.side1 + self.side2 + self.side3
        return self.t_perimeter

    def rectangle_perimeter(self):
        '''
        A function that takes the input of the user and returns the perimeter of a rectangle
        :return: the perimeter of a rectnagle using input from the user
        '''
        self.width = float(self.width_input.text()) #Any positive int or float value
        self.length = float(self.length_input.text()) #Any positive int or float value
        self.r_perimeter = 2 * (self.width + self.length)
        return self.r_perimeter

    def circle_perimeter(self):
        '''
        A function that takes the input of the user and returns the perimeter of a circle
        :return: the perimeter of a circle using input from the user
        '''
        self.radius = float(self.radius_input.text()) #Any positive int or float value
        self.c_perimeter = 2 * pi * self.radius
        return self.c_perimeter

    def calculate(self):
        '''
        A function for the calculate button that tells the program if the area or perimeter is being found and activites the input for the user
        '''
        if self.s_areabutton.isChecked() == True:
            self.side_input.setEnabled(True)
            self.side_label.setText('Side:')
        if self.t_areabutton.isChecked() == True:
            self.side1_input.setEnabled(True)
            self.side1_label.setText('Height:')
            self.side2_input.setEnabled(True)
            self.side2_label.setText('Base:')
        if self.r_areabutton.isChecked() == True:
            self.width_input.setEnabled(True)
            self.width_label.setText('Width:')
            self.length_input.setEnabled(True)
            self.length_label.setText('Length:')
        if self.c_areabutton.isChecked() == True:
            self.radius_input.setEnabled(True)
            self.radius_label.setText('Radius:')

        if self.s_perimeterbutton.isChecked() == True:
            self.side_input.setEnabled(True)
            self.side_label.setText('Side:')
        if self.t_perimeterbutton.isChecked() == True:
            self.side1_input.setEnabled(True)
            self.side1_label.setText('Side 1:')
            self.side2_input.setEnabled(True)
            self.side2_label.setText('Side 2:')
            self.side3_input.setEnabled(True)
            self.side3_label.setText('Side 3:')
        if self.r_perimeterbutton.isChecked() == True:
            self.width_input.setEnabled(True)
            self.width_label.setText('Width:')
            self.length_input.setEnabled(True)
            self.length_label.setText('Length:')
        if self.c_perimeterbutton.isChecked() == True:
            self.radius_input.setEnabled(True)
            self.radius_label.setText('Radius:')

    def submit(self):
        '''
        A function for the sumbit button that takes the values from the user and finds the area or perimeter and display the output. Also checks to make sure the the value is positive and either an int or float
        '''
        try:
            if self.s_areabutton.isChecked() == True:
                self.square_area()
                if self.side > 0:
                    self.s_output.setText(f'The area of a square with a \t\n'
                                            f'side of {self.side} = {self.s_area}\n')
                elif self.side < 0:
                    self.s_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.t_areabutton.isChecked() == True:
                self.triangle_area()
                if self.side1 > 0 and self.side2 > 0:
                    self.t_output.setText(f'The area of a triangle with a \t\n'
                                            f'height of {self.side1} and base of {self.side2} = {self.t_area}\n')
                elif self.side1 < 0 or self.side2 < 0:
                    self.t_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.r_areabutton.isChecked() == True:
                self.rectangle_area()
                if self.width > 0 and self.length > 0:
                    self.r_output.setText(f'The area of a rectangle with a \t\n'
                                            f'width of {self.width} and length of {self.length} = {self.r_area}\n')
                elif self.width < 0 or self.length < 0:
                    self.r_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.c_areabutton.isChecked() == True:
                self.circle_area()
                if self.radius > 0:
                    self.c_output.setText(f'The area of a circle with a \t\n'
                                            f'radius of {self.radius} = {round(self.c_area, 2)}\n')
                elif self.radius < 0:
                    self.c_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')

            if self.s_perimeterbutton.isChecked() == True:
                self.square_perimeter()
                if self.side > 0:
                    self.s_output.setText(f'The perimeter of a square with a \t\n'
                                            f'side of {self.side} = {self.s_perimeter}\n')
                elif self.side < 0:
                    self.s_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.t_perimeterbutton.isChecked() == True:
                self.triangle_perimeter()
                if self.side1 > 0 and self.side2 > 0 and self.side3 > 0:
                    self.t_output.setText(f'The perimeter of a triangle with the \t\n'
                                            f'sides of {self.side1}, {self.side2}, {self.side3} = {self.t_perimeter}\n')
                elif self.side1 < 0 or self.side2 < 0 or self.side3 < 0:
                    self.t_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.r_perimeterbutton.isChecked() == True:
                self.rectangle_perimeter()
                if self.width > 0 and self.length > 0:
                    self.r_output.setText(f'The perimeter of a rectangle with a \t\n'
                                            f'width of {self.width} and length of {self.length} = {self.r_perimeter}\n')
                elif self.width < 0 or self.length < 0:
                    self.r_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')
            if self.c_perimeterbutton.isChecked() == True:
                self.circle_perimeter()
                if self.radius > 0:
                    self.c_output.setText(f'The perimeter of a circle with a \t\n'
                                            f'radius of {self.radius} = {round(self.c_perimeter, 2)}\n')
                elif self.radius < 0:
                    self.c_output.setText(f'The value needs to be a positive numeric value\t\n'
                                          f'e.g.  1, 2, 3, etc.')

        except ValueError:
            self.clear()
            self.s_output.setText(f'The value needs to be a numeric value\t\n'
                                  f'e.g.  1, 2, 3, etc.')
            self.t_output.setText(f'The value needs to be a numeric value\t\n'
                                  f'e.g.  1, 2, 3, etc.')
            self.r_output.setText(f'The value needs to be a numeric value\t\n'
                                  f'e.g.  1, 2, 3, etc.')
            self.c_output.setText(f'The value needs to be a numeric value\t\n'
                                  f'e.g.  1, 2, 3, etc.')

    def clear(self):
        '''
        A function for the clear button that completely wipes everything out
        '''
        self.side_label.setText('')
        self.side_input.setText('')
        self.side_input.setEnabled(False)
        self.s_output.setText('')
        if self.s_areabutton.isChecked() == True:
            self.s_areabutton.setAutoExclusive(False)
            self.s_areabutton.setChecked(False)
            self.s_areabutton.setAutoExclusive(True)
        if self.s_perimeterbutton.isChecked() == True:
            self.s_perimeterbutton.setAutoExclusive(False)
            self.s_perimeterbutton.setChecked(False)
            self.s_perimeterbutton.setAutoExclusive(True)

        self.side1_label.setText('')
        self.side1_input.setText('')
        self.side1_input.setEnabled(False)
        self.side2_label.setText('')
        self.side2_input.setText('')
        self.side2_input.setEnabled(False)
        self.side3_label.setText('')
        self.side3_input.setText('')
        self.side3_input.setEnabled(False)
        self.t_output.setText('')
        if self.t_areabutton.isChecked() == True:
            self.t_areabutton.setAutoExclusive(False)
            self.t_areabutton.setChecked(False)
            self.t_areabutton.setAutoExclusive(True)
        if self.t_perimeterbutton.isChecked() == True:
            self.t_perimeterbutton.setAutoExclusive(False)
            self.t_perimeterbutton.setChecked(False)
            self.t_perimeterbutton.setAutoExclusive(True)

        self.width_label.setText('')
        self.width_input.setText('')
        self.width_input.setEnabled(False)
        self.length_label.setText('')
        self.length_input.setText('')
        self.length_input.setEnabled(False)
        self.r_output.setText('')
        if self.r_areabutton.isChecked() == True:
            self.r_areabutton.setAutoExclusive(False)
            self.r_areabutton.setChecked(False)
            self.r_areabutton.setAutoExclusive(True)
        if self.r_perimeterbutton.isChecked() == True:
            self.r_perimeterbutton.setAutoExclusive(False)
            self.r_perimeterbutton.setChecked(False)
            self.r_perimeterbutton.setAutoExclusive(True)

        self.radius_label.setText('')
        self.radius_input.setText('')
        self.radius_input.setEnabled(False)
        self.c_output.setText('')
        if self.c_areabutton.isChecked() == True:
            self.c_areabutton.setAutoExclusive(False)
            self.c_areabutton.setChecked(False)
            self.c_areabutton.setAutoExclusive(True)
        if self.c_perimeterbutton.isChecked() == True:
            self.c_perimeterbutton.setAutoExclusive(False)
            self.c_perimeterbutton.setChecked(False)
            self.c_perimeterbutton.setAutoExclusive(True)