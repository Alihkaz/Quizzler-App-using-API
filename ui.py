#
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

  def __init__(self,quiz_brain:QuizBrain):# here we are just saying that the quiz brain have a data type QuizBrain , its same as the data types wich we have speaked about in  this day !

    
    
    self.quiz=quiz_brain#here we are creating an object called quiz from the class Quiz_brain which is the data type of the quiz_brain file or library , and here the quiz will be equal as output to the quiz object in the main .py
    
    
    self.window=Tk()
    self.window.title("Quizller")
    self.window.config(padx=30, pady=30, bg=THEME_COLOR )

    # canvas
    
    self.canvas = Canvas(width=300, height=250)
    self.question_text = self.canvas.create_text(145, 130,width=280 ,text="Test Test", font=("Ariel", 20, "italic"),fill="black")#here we add the width to let the text fits inside the canvas. 
    self.canvas.config(bg="white", highlightthickness=0)
    self.canvas.grid(row=1, column=0, columnspan=2,pady=30)

    #buttons
    
    self.true_image = PhotoImage(file="true.png")
    self.true_button = Button(image=self.true_image, highlightthickness=0,command=self.true_pressed)
    self.true_button.grid(row=2, column=1)
    
    self.false_image = PhotoImage(file="false.png")
    self.false_button = Button(image=self.false_image, highlightthickness=0,command=self.false_pressed)
    self.false_button.grid(row=2, column=0)

    #labels

    self.score_label=Label(text=f"score: {0}", font=("Ariel",15, "italic"),bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)
    
    self.get_next_question()

    self.window.mainloop()
    

  def get_next_question(self):#this method is going to tap into the quizbrain class and call the next question method 
    self.canvas.config(bg="white")# reseting the color to white after displaying the color depending on the user answer and feedback
    
    if self.quiz.still_has_questions():
      
      self.canvas.config(bg="white")# reseting the color to white after displaying the color depending on the user answer and feedback
  
      self.score_label.config(text=f"Score: {self.quiz.score}")
    
      q_text=self.quiz.next_question()#here the object cretaed from the class has a method called get next question , and we call it as a method , and since it will give us an output as number of question and content we will aim to save it inside a variable called q text which will be passed inside the canvas configuration 
      self.canvas.itemconfig(self.question_text,text=q_text)

    else:

      self.canvas.itemconfig(self.question_text,text="you've reached the end of the quiz")
      self.true_button.config(state="disabled")
      self.false_button.config(state="disabled")#turning off the buttoms


  def true_pressed(self):
    
    is_right=self.quiz.check_answer("True")#once the true botton is triggerd we can get access to the quiz class which we have defined it above and get access to all its methods , and from that method is the check answer method , and here as an input for the function check , we pass as a logical approach the true word as an input to it as the true button is triggered which means its true , and vice versa for the false button , but we command it and used mit below instead 
    
    self.give_feedback( is_right)#what we are aiming for is once we get the result of that question , and once the buttom is triggered , we will aim to make something more through the feed back method like changing thye canvas color ! 

  def false_pressed(self):
    is_right=self.quiz.check_answer("False")#the is right variable is used to get the checking of the answer if its true or false as its saved in the question bank 
    self.give_feedback(is_right)

  def give_feedback(self,is_right):

      if is_right :
        self.canvas.config(bg="green")
      else:
        self.canvas.config(bg="red")#here if the question is true and i pressed on the x buttom , then my answer is false , not that if i press on x then its red or if i press on check button then it gives green , no , it depends on the answer of the question compared to the user answer . 
        
      self.window.after(1000,self.get_next_question)# after the screen being changed for either g or r , wait one second , and apply the next question method . 

    
    
    
  
  




