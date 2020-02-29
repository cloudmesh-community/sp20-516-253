# AWA Rekognition sp20-516-253, Arivukadal, Lenin

:o2: bibtex missing

:o2: spaces after context switch missing

:o2: no : at end of headings

## Amazon Rekognition overview

Amazon Rekognition is mainly used to include image and video analysis to your applications using highly scalable and deep learning technologies and you dont have to possess a machine learning expert to use it. With Amazon Rekognition, you can identify objects, people, text, scenes, and activities in images and videos, as well as detect any inappropriate content. Not only that - Amazon Rekognition also provides highly accurate facial analysis and facial search capabilities that you can use to detect, analyze, and compare faces for a wide variety of user verification, people counting, and public safety use cases.

## Amazon Rekognition key features

we have variety of key features with Amazon Rekognition and let us discuss the topics in details.

1. Labels
2. Custom labels.
3. Content moderation.
4. Text detection
5. Face detection and analysis.
6. Celebrity recognition.
7. Pathing.

## Labels

Identifying objects (such as bike, telephone, building), and scenes (such as parking lot, beach, city) is easy using Amazon Rekognition. Also when analyzing video, you can identify specific activities such as "delivering a package" or "playing soccer".

## Custom labels

As stated by its name *labels* finding corporate logo in social media, identify your products on store shelves, classify your machine parts in an assembly line, or detect your animated characters in videos.With Amazon Rekognition Custom Labels, you can extend the detection capabilities of Amazon Rekognition to extract information from images that is uniquely helpful to your business.

## Content moderation

Amazon Rekognition helps you identify potentially unsafe or inappropriate content across both image and video assets and provides you with detailed labels that allow you to accurately control what you want to allow based on your needs.

## Text detection

This can be useful in many ways for exaomle in photos, text appears very differently than neat words on a printed page. Amazon Rekognition can read skewed and distorted text to capture information like store names, street signs, and text on product packaging.

## Face detection and analysis

With Amazon Rekognition, you can easily detect when faces appear in images and videos and get attributes such as gender, age range, eyes open, glasses, facial hair for each. In video, you can also measure how these face attributes change over time, such as constructing a timeline of the emotions expressed by an actor.

## Face search and verification

Although this face search an verification was in constant development with AWS recognition and by providing a fast and accurate face search, AWS recognition will allow you to identify a person in a photo or video using your private repository of face images. Not only that you can also verify identity by analyzing a face image against images you have stored for comparison.

## Celebrity recognition

Its an interesting use case used on variuos way. You can quickly identify well known people in your video and image libraries to catalog footage and photos for marketing, advertising, and media industry use cases. 

## Pathing

You can capture the path of people in the scene when using Amazon Rekognition with video files. For example, you can use the movement of athletes during a game to identify plays for post-game analysis. 


## We know about AWS recognition  but what is Rekognition Image & Video? 


Rekognition Video is a video recognition service that detects activities; understands the movement of people in frame; and recognizes objects, celebrities, and inappropriate content in videos stored in Amazon S3 and live video streams from Acuity. Rekognition Video detects persons and tracks them through the video even when their faces are not visible, or as the whole person might go in and out of the scene. For example, this could be used in an application that sends a real-time notification when someone delivers a package to your door. Rekognition Video allows you also to index metadata like objects, activities, scene, celebrities, and faces that make video search easy. 

Rekognition Image uses deep neural network models to detect and label thousands of objects and scenes in your images, and we are continually adding new labels and facial recognition features to the service. With Rekognition Image, you only pay for the images you analyze and the face metadata you store.



#### How many images are needed to train a custom model?

we need to have variability of the custom labels and number of images required to train a custom model to predict and the quality of the training data. If you already have a high number of labeled images, we recommend training a model with as many images as you have available. Please refer to the documentation for limits on maximum training dataset size.For example, a distinct logo overlaid on an image can be detected with 1-2 training images, while a more subtle logo required to be detected under many variations (scale, viewpoint, deformations) may need in the order of tens to hundreds of training examples with high quality annotations. .

You can always start with fewer images. For example - Although hundreds of images may sometimes be required to train a custom model with high accuracy, with Custom Labels you can first train a model with tens of images per label, review your test results to understand where it does not work, and accordingly add new training images and train again to iteratively improve your model.

#### Different Facial Rekognition methods

## 1. What is Facial Analysis?
Facial analysis is the process of detecting a face within an image and extracting relevant face attributes from it. Amazon Rekognition Image takes returns the bounding box for each face detected in an image along with attributes such as gender, presence of sunglasses, and face landmark points. Rekognition Video will return the faces detected in a video with timestamps and, for each detected face, the position and a bounding box along with face landmark points. 

## 2. What is Face Comparison?
Face Comparison is the process of comparing one face to one or more faces to measure similarity. Using the CompareFaces API, Amazon Rekognition Image lets you measure the likelihood that faces in two images are of the same person. The API compares a face in the source input image with each face detected in the target input image and returns a similarity score for each comparison. You also get a bounding box and confidence score for each face detected. You can use face comparison to verify a person’s identity against their personnel photo on file in near real-time. 

## 3.What is Facial Recognition?
Facial recognition is the process of identifying or verifying a person’s identity by searching for their face in a collection of faces. Using facial recognition, you can easily build applications such as multi-factor authentication for bank payments, automated building entry for employees, and more.



#### Exciting Use cases

## Identify products, landmarks and brands

App developers can use Amazon Rekognition Custom Labels to identify specific items in social media and photo apps. For example, you could train a custom model to identify famous landmarks in a city to provide tourists with information about its history, operating hours, and ticket prices by simply taking a photo. 

## Analyze shopper patterns

With Amazon Rekognition, you can analyze shopper behavior and density in your retail store by studying the path that each person follows. Using face analysis, you can also understand the average age ranges, gender distribution and emotions expressed by the people, without identifying them.





