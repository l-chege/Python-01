class User:
    def __init__(self, user_email, user_name, password, current_job_title):        #constructor function to initialize class
        self.email = user_email
        self.name = user_name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):                    #function to change password
        self.password = new_password
    

    def change_job_title(self, new_job_title):                 #function to change job title
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")

app_user_one = User("lc@lc.com", "lchege", "password10", "cloud engineer")         #creating an instance of the class (object)
app_user_one.get_user_info()                                                        #calling the get_user_info function on the object

app_user_one.change_job_title("DevOps Engineer")                                    #calling the change_job_title function on the object
app_user_one.get_user_info()                                                        #calling the get_user_info function on the object

app_user_two = User("nn@nn.com", "nana", "password20", "cloud engineer")          #creating an instance of the class (object)
app_user_two.get_user_info()                                                       #calling the get_user_info function on the object