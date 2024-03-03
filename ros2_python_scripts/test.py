import speech_recognition as sr
import pyttsx3

# def recognize_speech():
#     # Initialize recognizer
#     recognizer = sr.Recognizer()

#     # Capture audio from the microphone
#     with sr.Microphone() as source:
#         print("Listening...")

#         # Adjust for ambient noise
#         recognizer.adjust_for_ambient_noise(source)

#         # Listen to the user's input
#         audio_data = recognizer.listen(source)

#         print("Recognizing...")

#         try:
#             # Recognize the speech using Google Speech Recognition
#             text = recognizer.recognize_google(audio_data)
#             print("You said:", text)
#         except sr.UnknownValueError:
#             print("Sorry, could not understand audio.")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))

# if __name__ == "__main__":
#     recognize_speech()



# def text_to_speech(text, rate=150):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()
#     engine.setProperty('voice', -2)
#     # Set speech rate (words per minute)
#     engine.setProperty('rate', rate)

#     # Convert text to speech
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()

# if __name__ == "__main__":
#     text = input("Enter the text to convert to speech: ")
#     text_to_speech(text)




#--------------------------/plan --------------------------

# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import Path
# from geometry_msgs.msg import PoseStamped

# class PlanSubscriber(Node):

#     def __init__(self):
#         super().__init__('plan_subscriber')
#         self.subscription = self.create_subscription(
#             Path,
#             '/plan',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         self.get_logger().info('Received plan with {} poses'.format(len(msg.poses)))
#         for i, pose in enumerate(msg.poses):
#             x = pose.pose.position.x
#             y = pose.pose.position.y
#             self.get_logger().info('Pose {}: x={}, y={}'.format(i, x, y))

# def main(args=None):
#     rclpy.init(args=args)
#     plan_subscriber = PlanSubscriber()
#     try:
#         rclpy.spin(plan_subscriber)
#     except KeyboardInterrupt:
#         pass
#     plan_subscriber.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()



#-------------------- '/odom'-----------------


# import rclpy
# from rclpy.node import Node
# from nav_msgs.msg import Odometry

# class PositionSubscriber(Node):

#     def __init__(self):
#         super().__init__('position_subscriber')
#         self.current_x = None
#         self.current_y = None
#         self.subscription = self.create_subscription(
#             Odometry,
#             '/odom',  # Replace with the appropriate topic for your robot
#             self.odometry_callback,
#             10)

#     def odometry_callback(self, msg):
#         # Extract the x and y values from the received odometry message
#         self.current_x = msg.pose.pose.position.x
#         self.current_y = msg.pose.pose.position.y
#         self.get_logger().info('Current position - x: {}, y: {}'.format(self.current_x, self.current_y))

# def main(args=None):
#     rclpy.init(args=args)
#     position_subscriber = PositionSubscriber()
#     try:
#         rclpy.spin(position_subscriber)
#     except KeyboardInterrupt:
#         pass
#     position_subscriber.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()




#----------------------------/goal_pose ----------------------------

# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import PoseStamped

# class GoalPoseSubscriber(Node):

#     def __init__(self):
#         super().__init__('goal_pose_subscriber')
#         self.subscription = self.create_subscription(
#             PoseStamped,
#             '/goal_pose',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         x = msg.pose.position.x
#         y = msg.pose.position.y
#         self.get_logger().info('Received goal pose - x: {}, y: {}'.format(x, y))


# def main(args=None):
#     rclpy.init(args=args)
#     goal_pose_subscriber = GoalPoseSubscriber()
#     try:
#         rclpy.spin(goal_pose_subscriber)
#     except KeyboardInterrupt:
#         pass
#     goal_pose_subscriber.destroy_node()
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()
