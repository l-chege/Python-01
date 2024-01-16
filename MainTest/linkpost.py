from user import User
from post import Post   


app_user_one = User("lc@lc.com", "lchege", "password10", "cloud engineer")         #creating an instance of the class (object)
app_user_one.get_user_info()                                                        #calling the get_user_info function on the object

app_user_one.change_job_title("DevOps Engineer")                                    #calling the change_job_title function on the object
app_user_one.get_user_info()                                                        #calling the get_user_info function on the object

app_user_two = User("nn@nn.com", "nana", "password20", "cloud engineer")          #creating an instance of the class (object)
app_user_two.get_user_info()                                                       #calling the get_user_info function on the object

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
