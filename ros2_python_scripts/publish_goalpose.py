
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import speech_recognition as sr
import pyttsx3



class GoalPosePublisher(Node):

    def __init__(self):
        super().__init__('goal_pose_publisher')
        self.publisher_ = self.create_publisher(PoseStamped, '/goal_pose', 10)
        # self.subscription = self.create_subscription(
        #     Odometry,
        #     '/odom',  # Replace with the appropriate topic for your robot
        #     self.odometry_callback,
        #     10)

        self.timer_ = self.create_timer(1, self.locations)  # Replace 0.1 with your desired frequency
        # self.current_x = None
        # self.current_y = None

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        # self.pos_vals= [0.0,0.0]

    # def odometry_callback(self, msg):
    # # Extract the x and y values from the received odometry message
    #     self.current_x = msg.pose.pose.position.x
    #     self.current_y = msg.pose.pose.position.y
    #     if int(self.current_x) == 4:
    #         self.text_to_speech("reached to hall")
        # self.get_logger().info('Current position - x: {}, y: {}'.format(self.current_x, self.current_y))


    def speech_func(self):
        with sr.Microphone() as source:
             print("Listening...")
             self.recognizer.adjust_for_ambient_noise(source)
             audio_data = self.recognizer.listen(source)
            #  print("Recognizing...")
        try:
            # Recognize the speech using Google Speech Recognition
            text = self.recognizer.recognize_google(audio_data)
            print("Next Destination :", text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            text = " "
        return text.lower()


    def locations(self):
        text = self.speech_func()

        hall         =  [4.0,-3.0]
        bedroom      =  [8.9,2.5]
        guest_room   =  [12.5,-4.4]
        dining_room =  [15.0,3.09]
        kitchen      =  [18.36,-1.02]
        home         =  [0.0,0.0]

        if "hall" in text:
            self.text_to_speech("Ok sir moving to hall")
            self.publish_goal_pose(hall[0],hall[1])
        elif "bedroom" in text:
            self.text_to_speech("Ok sir moving to bedroom")
            self.publish_goal_pose(bedroom[0],bedroom[1])
        elif "guest" in text:
            self.text_to_speech("Ok sir moving to guestroom")
            self.publish_goal_pose(guest_room[0],guest_room[1])
        elif "dinning" in text:
            self.text_to_speech("Ok sir moving to dinning room")
            self.publish_goal_pose( dining_room[0], dining_room[1])
        elif "kitchen" in text:
            self.text_to_speech("Ok sir moving to kitchen")
            self.publish_goal_pose(kitchen[0],kitchen[1])
        elif "home" in text:
            self.text_to_speech("Ok sir moving to home")
            self.publish_goal_pose(home[0],home[1])
        elif "close" in text:
            exit()
        else:
            print("No Destination")
            
    def text_to_speech(self,text, rate=150):
        self.engine.setProperty('rate', rate)
        self.engine.say(text)
        self.engine.runAndWait()

    def publish_goal_pose(self,x_val,y_val):
        # Create the PoseStamped message here, filling in the position and orientation fields
        # based on your data source and requirements
        # print("Published",self.pos_vals[0],self.pos_vals[1])
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'  # Replace with appropriate frame ID
        goal_pose.pose.position.x = x_val # Replace with actual position values
        goal_pose.pose.position.y = y_val
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0.0  # Replace with actual orientation values
        goal_pose.pose.orientation.y = 0.0
        goal_pose.pose.orientation.z = 0.0
        goal_pose.pose.orientation.w = 1.0
        self.publisher_.publish(goal_pose)
        

def main(args=None):
   
    rclpy.init(args=args)
    node = GoalPosePublisher()
    node.locations()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':

    main()


