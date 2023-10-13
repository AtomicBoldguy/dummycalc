import customtkinter
import ctypes
import locale

myappid = 'IK15.SanychCalc.1'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("calculator.ico")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode('Dark')

        self.title("Калькулятор 'для Саныча СРОЧНО! :)' ")
        self.geometry("550x350")
        self.attributes("-topmost", True)
        self.iconbitmap('./calculator.ico')

        # set grid layout 1x2
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, rowspan=8, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        # self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="пип пуп пип",
        #                                                      compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Найти процент от числа",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="center", command=self.home_button_event, compound="left")
        self.home_button.grid(row=0, column=0, sticky="nsew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Сколько процентов составляет\rодно число от другого числа",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="left", command=self.frame_2_button_event, compound="left")
        self.frame_2_button.grid(row=1, column=0, sticky="w", padx=0)

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Прибавить процент к числу",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="center", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=2, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Вычесть процент из числа",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="center", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=3, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="На сколько процентов\rодно число больше другого",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="center", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=4, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="На сколько процентов\rодно число меньше другого",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="center", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=5, column=0, sticky="ew")

        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Найти 100 процентов",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="center", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=6, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_rowconfigure(6, weight=1)
        self.home_frame.grid_columnconfigure(4, weight=1)

        self.entry_1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Процент", width=100)
        self.entry_1.grid(row=0, column=0, padx=(45, 0), pady=(20, 20), sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.home_frame, text="ОТ", anchor="nw", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Числа", width=100)
        self.entry_2.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2.bind("<Return>", lambda event: self.res(event,one=self.entry_2.get(),two=self.entry_1.get()))
        self.entry_1.bind("<Return>", lambda event: self.res(event,one=self.entry_2.get(),two=self.entry_1.get()))
        self.entry_1.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Вычислить", compound="right", command=lambda: self.res(one=self.entry_2.get(),two=self.entry_1.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=3, padx=(45, 0), pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_rowconfigure(5, weight=1)
        self.second_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_2 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Число 1", width=100)
        self.entry_1_2.grid(row=0, column=0, padx=(45, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.second_frame, text="ОТ", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_2 = customtkinter.CTkEntry(self.second_frame, placeholder_text="Числа 2", width=100)
        self.entry_2_2.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_2.bind("<Return>", lambda event: self.res2(event,one=self.entry_1_2.get(),two=self.entry_2_2.get()))
        self.entry_1_2.bind("<Return>", lambda event: self.res2(event,one=self.entry_1_2.get(),two=self.entry_2_2.get()))
        self.entry_1_2.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_2.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res2(one=self.entry_1_2.get(),
                                                                                    two=self.entry_2_2.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=(45, 0), pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_rowconfigure(5, weight=1)
        self.third_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_3 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Процентов", width=100)
        self.entry_1_3.grid(row=0, column=0, padx=(45, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.third_frame, text="К", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_3 = customtkinter.CTkEntry(self.third_frame, placeholder_text="Числу", width=100)
        self.entry_2_3.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_3.bind("<Return>", lambda event: self.res3(event,one=self.entry_1_3.get(),two=self.entry_2_3.get()))
        self.entry_1_3.bind("<Return>", lambda event: self.res3(event,one=self.entry_1_3.get(),two=self.entry_2_3.get()))
        self.entry_1_3.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_3.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.third_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res3(one=self.entry_1_3.get(),
                                                                                    two=self.entry_2_3.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=(45, 0), pady=10)
        # create third frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_rowconfigure(5, weight=1)
        self.fourth_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_4 = customtkinter.CTkEntry(self.fourth_frame, placeholder_text="Процентов", width=100)
        self.entry_1_4.grid(row=0, column=0, padx=(45, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.fourth_frame, text="ОТ", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_4 = customtkinter.CTkEntry(self.fourth_frame, placeholder_text="Числа", width=100)
        self.entry_2_4.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_4.bind("<Return>", lambda event: self.res4(event,one=self.entry_1_4.get(),two=self.entry_2_4.get()))
        self.entry_1_4.bind("<Return>", lambda event: self.res4(event,one=self.entry_1_4.get(),two=self.entry_2_4.get()))
        self.entry_1_4.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_4.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.fourth_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res4(one=self.entry_1_4.get(),
                                                                                    two=self.entry_2_4.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=(45, 0), pady=10)
        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_rowconfigure(5, weight=1)
        self.fifth_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_5 = customtkinter.CTkEntry(self.fifth_frame, placeholder_text="Число 1", width=100)
        self.entry_1_5.grid(row=0, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.fifth_frame, text="БОЛЬШЕ", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_5 = customtkinter.CTkEntry(self.fifth_frame, placeholder_text="Числа 2", width=100)
        self.entry_2_5.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_5.bind("<Return>", lambda event: self.res5(event,one=self.entry_1_5.get(),two=self.entry_2_5.get()))
        self.entry_1_5.bind("<Return>", lambda event: self.res5(event,one=self.entry_1_5.get(),two=self.entry_2_5.get()))
        self.entry_1_5.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_5.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.fifth_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res5(one=self.entry_1_5.get(),
                                                                                    two=self.entry_2_5.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=20, pady=10)
        # create sixth frame
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_rowconfigure(5, weight=1)
        self.sixth_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_6 = customtkinter.CTkEntry(self.sixth_frame, placeholder_text="Число 1", width=100)
        self.entry_1_6.grid(row=0, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.sixth_frame, text="МЕНЬШЕ", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_6 = customtkinter.CTkEntry(self.sixth_frame, placeholder_text="Числа 2", width=100)
        self.entry_2_6.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_6.bind("<Return>", lambda event: self.res6(event,one=self.entry_1_6.get(),two=self.entry_2_6.get()))
        self.entry_1_6.bind("<Return>", lambda event: self.res6(event,one=self.entry_1_6.get(),two=self.entry_2_6.get()))
        self.entry_1_6.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_6.bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.sixth_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res6(one=self.entry_1_6.get(),
                                                                                    two=self.entry_2_6.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=20, pady=10)
        # create seventh frame
        self.seventh_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventh_frame.grid_rowconfigure(5, weight=1)
        self.seventh_frame.grid_columnconfigure(4, weight=1)

        self.entry_1_7 = customtkinter.CTkEntry(self.seventh_frame, placeholder_text="Число", width=100)
        self.entry_1_7.grid(row=0, column=0, padx=(45, 0), pady=(20, 20), sticky="nsew")
        self.appearance_mode_label = customtkinter.CTkLabel(self.seventh_frame, text="ЭТО", anchor="nw",
                                                            font=customtkinter.CTkFont(size=20, weight="normal"))
        self.appearance_mode_label.grid(row=0, column=1, padx=10, pady=(10, 0))
        self.entry_2_7 = customtkinter.CTkEntry(self.seventh_frame, placeholder_text="Процентов", width=100)
        self.entry_2_7.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        self.entry_2_7.bind("<Return>", lambda event: self.res7(event,one=self.entry_1_7.get(),two=self.entry_2_7.get()))
        self.entry_1_7.bind("<Return>", lambda event: self.res7(event,one=self.entry_1_7.get(),two=self.entry_2_7.get()))
        self.entry_1_7.bind("<Control-V>", self.entry_1.clipboard_append)
        self.entry_2_7 .bind("<Control-V>", self.entry_2.clipboard_append)

        self.home_frame_button_2 = customtkinter.CTkButton(self.seventh_frame, text="Вычислить", compound="right",
                                                           command=lambda: self.res7(one=self.entry_1_7.get(),
                                                                                    two=self.entry_2_7.get()))
        self.home_frame_button_2.grid(row=2, column=0, columnspan=4, padx=(45, 0), pady=10)

        #calc
        self.result_label = customtkinter.CTkLabel(self.home_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.second_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.third_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.fourth_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.fifth_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.sixth_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label = customtkinter.CTkLabel(self.seventh_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)

        self.calc_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.calc_frame.grid(column=1, row=3, rowspan=5, pady=(10, 0), sticky="nsew")
        self.calc_frame.grid_rowconfigure(5, weight=2)
        self.calc_frame.grid_columnconfigure(3, weight=2)

        self.entry_1_calc = customtkinter.CTkEntry(self.calc_frame, placeholder_text="", height=30, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.entry_1_calc.grid(row=0, column=0, padx=(35, 0), pady=(20, 20), sticky="nsew")

        # self.calc_type = customtkinter.CTkOptionMenu(self.calc_frame, dynamic_resizing=True,
        #                                              width=50,
        #                                             values=["+", "-", "*", "/"])
        # self.calc_type.grid(row=0, column=1, padx=10, pady=0)
        #
        #
        # self.entry_2_calc = customtkinter.CTkEntry(self.calc_frame, placeholder_text="Число 2", width=100)
        # self.entry_2_calc.grid(row=0, column=2, padx=0, pady=(20, 20), sticky="nsew")
        # self.entry_2_calc.bind("<Return>", lambda event: self.res_calc(event,one=self.entry_1_calc.get(),two=self.entry_2_calc.get()))
        # self.entry_1_calc.bind("<Return>", lambda event: self.res_calc(event,one=self.entry_1_calc.get()))
        # self.entry_1_calc.bind("<plus>", lambda event: self.res_calc(event,one=self.entry_1_calc.get()))

        self.entry_1_calc.bind("<Control-V>", self.entry_1_calc.clipboard_append)
        # self.entry_2_calc.bind("<Control-V>", self.entry_2_calc.clipboard_append)
        self.label_text1 = customtkinter.StringVar
        self.label_text1 = 0
        self.calc_result_label = customtkinter.CTkLabel(self.calc_frame, anchor="nw", text='0', font=customtkinter.CTkFont(size=25, weight="bold"))
        self.calc_result_label.grid(row=0, column=1, columnspan=2, padx=(25, 0), pady=10)
        # self.result = self.calc_result_label.getint(self.label_text1)
        self.strs = ''



        self.bind("<plus>", lambda event: self.calc(event, one=float(self.calc_result_label._text), two=float(self.entry_1_calc.get()[:self.entry_1_calc.get().find('+')]), znak='+'))
        self.bind("<minus>", lambda event: self.calc(event, one=float(self.calc_result_label._text), two=float(self.entry_1_calc.get()[:self.entry_1_calc.get().find('-')]), znak='-'))
        self.bind("<*>", lambda event: self.calc(event, one=float(self.calc_result_label._text), two=float(self.entry_1_calc.get()[:self.entry_1_calc.get().find('*')]), znak='*'))
        self.bind("</>", lambda event: self.calc(event, one=float(self.calc_result_label._text), two=float(self.entry_1_calc.get()[:self.entry_1_calc.get().find('/')]), znak='/'))

        self.calc_result_label.bind("<Button-1>", self.copy_text_to_clipboard_calc)

        # self.calc_result_label = customtkinter.CTkLabel(self.second_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        # self.calc_result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        # self.calc_result_label.bind("<Button-1>", self.copy_text_to_clipboard)
        # self.calc_button = customtkinter.CTkButton(self.calc_frame, text="Вычислить", compound="right",
        #                                                    command=lambda: self.res6(one=self.entry_1_6.get(),
        #                                                                             two=self.entry_2_6.get()))
        # self.calc_button.grid(row=2, column=0, columnspan=4, padx=20, pady=10)
        # self.calc_result_label = customtkinter.CTkLabel(self.calc_frame, anchor="nw", text="", font=customtkinter.CTkFont(size=20, weight="normal"))
        # self.calc_result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)

        self.entry_2.bind("<Left>", lambda event: self.entry_1.focus_set())
        self.entry_1.bind("<Right>", lambda event: self.entry_2.focus_set())

        self.entry_2_2.bind("<Left>", lambda event: self.entry_1_2.focus_set())
        self.entry_1_2.bind("<Right>", lambda event: self.entry_2_2.focus_set())

        self.entry_2_3.bind("<Left>", lambda event: self.entry_1_3.focus_set())
        self.entry_1_3.bind("<Right>", lambda event: self.entry_2_3.focus_set())

        self.entry_2_4.bind("<Left>", lambda event: self.entry_1_4.focus_set())
        self.entry_1_4.bind("<Right>", lambda event: self.entry_2_4.focus_set())

        self.entry_2_6.bind("<Left>", lambda event: self.entry_1_6.focus_set())
        self.entry_1_6.bind("<Right>", lambda event: self.entry_2_6.focus_set())

        self.entry_2_5.bind("<Left>", lambda event: self.entry_1_5.focus_set())
        self.entry_1_5.bind("<Right>", lambda event: self.entry_2_5.focus_set())

        self.entry_2_6.bind("<Left>", lambda event: self.entry_1_7.focus_set())
        self.entry_1_6.bind("<Right>", lambda event: self.entry_2_7.focus_set())

        # select default frame
        self.select_frame_by_name("frame_1")

    def calc(self, event="", one=0, two=0, znak=''):
        self.entry_1_calc.delete(0,20)
        self.calc_result_label.destroy()

        if int(one) != 0:
            self.strs += f'{znak}{int(two)}'
        else:
            self.strs += f'{int(two)}'

        self.actions_label = customtkinter.CTkLabel(self.calc_frame, anchor="nw", text=f'{self.strs}',
                                                    font=customtkinter.CTkFont(size=15, weight="normal"))
        self.actions_label.grid(row=2, column=0, padx=(35, 0), pady=10)

        if znak == '+':
            self.result = one + two
        elif znak == '-':
            self.result = one - two
        elif znak == '/':
            if one == 0:
                self.result = two
            else:
                self.result = one / two
        elif znak == '*':
            if one == 0:
                self.result = 1 * two
            else:
                self.result = one * two

        self.calc_result_label = customtkinter.CTkLabel(self.calc_frame, anchor="nw", text=f'{self.result}',
                                                        font=customtkinter.CTkFont(size=25, weight="bold"))
        self.calc_result_label.grid(row=0, column=1, columnspan=2, padx=(25, 0), pady=10)
        self.calc_result_label.bind("<Button-1>", self.copy_text_to_clipboard_calc)

    def res_calc(self, event="", one="", res=0):
        # self.label_text = customtkinter.StringVar()
        # res = 0
        print(one)
        pos = one.find("+")
        temp = one[pos+1:]
        pos1 = temp.find("+")
        if pos1 != -1:
            if pos != -1:
                print(one[:pos], temp[:temp.find("+")])
                res = res + (int(one[:pos])+int(temp[:temp.find("+")]))
                print(res)
                self.res_calc(one=temp, res=res)
            else:
                print('fso')
        else:
            print('fso1')

        # if self.calc_type._current_value == '+':
        #     self.label_text.set(str((float(one)+(float(two)))))
        # elif self.calc_type._current_value == '-':
        #     self.label_text.set(str(round((float(one) - (float(two))), 1)))
        # elif self.calc_type._current_value == '*':
        #     self.label_text.set(str(round((float(one) * (float(two))), 1)))
        # elif self.calc_type._current_value == '/':
        #     self.label_text.set(str(round((float(one) / (float(two))), 1)))
        # self.calc_result_label = customtkinter.CTkLabel(self.second_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        # self.calc_result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        # self.calc_result_label.bind("<Button-1>", self.copy_text_to_clipboard)

    def res(self, event="", one=1, two=1):
        self.result_label.destroy()

        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(round(float(one)*(float(two)/100),1)))
        self.result_label = customtkinter.CTkLabel(self.home_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label.bind("<Button-1>", self.copy_text_to_clipboard)

    def res2(self, event="", one=1, two=1):
        self.result_label.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(round((float(one)/(float(two))*100),1))+"%")
        self.result_label_2 = customtkinter.CTkLabel(self.second_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_2.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label_2.bind("<Button-1>", self.copy_text_to_clipboard)

    def res3(self, event="", one=1, two=1):
        self.result_label_3.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(float((float(two)*(1+(float(one)/100))))))
        self.result_label_3 = customtkinter.CTkLabel(self.third_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_3.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label_3.bind("<Button-1>", self.copy_text_to_clipboard)

        # fourth frame (input fields and buttons for third calculation)
        # self.fourth_frame = tk.Frame(self._root, bg="#ffffff")
        # self.fourth_frame.pack(fill='both', expand=True)
        #
        # self.entry_field_three = CTkEntryField(master=self.fourth_frame, width=67, corner_radius=8, fg_color=rgb((90, 90, 90)), borderless=False, justify="center", placeholder_text="", state="readonly").place(relwidth=.95, relheight=1.)
        # self.button_clear_all = ttk.Button(
        #     master=self.fourth_frame,
        #     image=self.icon_deleteAll,
        #     style="Toolbutton",
        #     command=lambda: [
        #         self.entry_field_three["state"] = "normal" if not bool(len([i for i in list(self.entry_field_three.get())])) else 'disabled' ,
        #         self.entry_field_three.update(),
        #
        #         self.entry_field_one['state'] = "normal" if len(list(self.entry_

    def res4(self, event="", one=1, two=1):
        self.result_label_4.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(float((float(two)*(1-(float(one)/100))))))
        self.result_label_4 = customtkinter.CTkLabel(self.fourth_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_4.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label_4.bind("<Button-1>", self.copy_text_to_clipboard)

    def res5(self, event="", one=1, two=1):
        self.result_label_5.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(round(float((float(one)/float(two)*100-100)),1))+'%')
        self.result_label_5 = customtkinter.CTkLabel(self.fifth_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_5.grid(row=3, column=0, columnspan=4, padx=(20, 0), pady=10)
        self.result_label_5.bind("<Button-1>", self.copy_text_to_clipboard)

    def res6(self, event="", one=1, two=1):
        self.result_label_6.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set(str(round(float(100-((float(one)/float(two)*100))),1))+'%')
        self.result_label_6 = customtkinter.CTkLabel(self.sixth_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_6.grid(row=3, column=0, columnspan=4, padx=(20, 0), pady=10)
        self.result_label_6.bind("<Button-1>", self.copy_text_to_clipboard)

    def res7(self, event="", one=1, two=1):
        self.result_label_7.destroy()
        self.label_text = customtkinter.StringVar()
        self.label_text.set('100% - это '+str(float(int(one)*(100/float(two)))))
        self.result_label_7 = customtkinter.CTkLabel(self.seventh_frame, anchor="nw", textvariable=self.label_text, font=customtkinter.CTkFont(size=20, weight="normal"))
        self.result_label_7.grid(row=3, column=0, columnspan=4, padx=(45, 0), pady=10)
        self.result_label_7.bind("<Button-1>", self.copy_text_to_clipboard)

    def copy_text_to_clipboard(self, event):
        field_value = self.label_text.get()  # get field value from event, but remove line return at end
        self.clipboard_clear()  # clear clipboard contents
        self.clipboard_append(field_value)  # append new value to clipbaord

    def copy_text_to_clipboard_calc(self, event):
        field_value = self.calc_result_label._text  # get field value from event, but remove line return at end
        self.clipboard_clear()  # clear clipboard contents
        self.clipboard_append(field_value)  # append new value to clipbaord

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "frame_1" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")

        # show selected frame
        if name == "frame_1":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
        if name == "frame_6":
            self.sixth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixth_frame.grid_forget()
        if name == "frame_7":
            self.seventh_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seventh_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("frame_1")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")

    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
