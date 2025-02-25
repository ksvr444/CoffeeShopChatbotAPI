# Instructions

- torch library works for lower versions 3.9-3.12
- create virtual environment by clicking the python icon in the bottom right corner
-  To deploy the Meta-Llama-3-8B-Instruct model for text generation in a localhost environment, you need to use the AutoModelForCausalLM class instead of AutoModelForSeq2SeqLM, as Llama models are causal language models designed for text generation
- miro.com for drawing architectures

# Architecture
- concatinating multiple tasks in one single prompt would lead to inaccuracies and the model loose stuff.
- so divide the tasks and each task is treated as agent.


# Some imp notes
- runpod has the ability to take the json content from test_input.json and run the test.
- After the test run we need to create a docker file to deploy that in runpod.
- docker is something like lightweight virtual machine and run it. install docker
- dockerhub is a respository of virtual machines that we host.
- Push our own virtual machines to push into docker hub and pull it from there.

# Docker
- you define a docker file
- that file has the instructions and preparation of the virtual machines(containers)
- convert it into an image (built version of docker file)
- running version of image is called container
- install docker extension to VS code
- right click on docker file and build the image
- run the below command to run the image
- - docker run -it \
        -e RUNPOD_TOKEN="rpa_1FL9QJOAXMCBI30EWAZJ13PN6B2OCT96EVALQNHH1jmqnj" \
        -e RUNPOD_CHATBOT_URL="https://api.runpod.ai/v2/vllm-q6vtpiamk6soqv/openai/v1" \
        -e RUNPOD_EMBEDDING_URL="https://api.runpod.ai/v2/tfnp6d22easxbs/openai/v1" \
        -e RUNPOD_EMBEDDING_TOKEN="rpa_OIGORVO074R6WAW8ICP7IFR8ZPDG3BDWKFK987Q61610we" \
        -e MODEL_NAME="meta-llama/Meta-Llama-3-8B-Instruct" \
        -e PINECONE_API_KEY="pcsk_7VzP6s_B8d2miS2zWEgcD7wXac89fQ5YaE8ywX4hJbLYShX6RfotWWhayZtttA2Kjv8yfF" \
        -e PINECONE_INDEX_NAME="coffeeshop" \
        chatbot

- build the docker image again.
- goto docker extension -> chatbot -> right clidk on latest -> push
- generate a token to docker hub and use username (ksvr44masters) and token to push into the docker hub
- check whethe the docker hub registry is registered correctly.
- Now the container is available in docker hub.
- this helps to install it on runpod quite easily

# Deploy in runppod
- goto runpod -> serverless -> new endpoint
- click docker image -> next
- create credential for container registry (give access token for password)
- copy paste the image name as ksvr444masters/chatbot
- select CPU
- To add/edit credentials Settings -> Container Registry Auth
- check for os version of docker image
- - docker manifest inspect --verbose ksvr444masters/chatbot_1:latest
- Usually in your macbook it creates and linux/arm image as its macbook. Runpod accepts linuc/amd64.
- To create the build
- -  docker build --pull --rm -f "python-code/api/Dockerfile" --platform linux/amd64 -t chatbot_1 "python-code/api" 
- Now this runpod endpoint is used as an api to receives messages from from frontend


# Frontend
- install node
- install expo go app in android to test 
- (its a library that helps to write the reactive native code with the help of libraries)
- https://docs.expo.dev/router/installation/
npx create-expo-app@latest
cd App
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
(https://stackoverflow.com/questions/66766591/expo-error-starting-tunnel-failed-to-install-expo-ngrok2-4-3-globally)
npm install @expo/ngrok@4.1.0
npx expo start --tunnel
- scan QR code in expo go app and view the application.
- To do a fresh start
npm run reset-project
- set main entry in package.sjon
- install native-wind (simplify css) (https://www.nativewind.dev/getting-started/expo-router)
- tailwind vscode extension "Tailwind css intellisense"
- Donot forget to include babel.config.js file
- create a figma design

# Google fonts
- Removing index is done in _layout.tsx file in return Stack
- download Sona fonts and load them in fonts

# fontend code
- install the extension 'ES7+ React/Redux/React-Native snippets'
- shortcut - rnfes and click, it autofills
- onPress={() => {router.push("/(tabs)/home)}} navigates to a page on pressing it.
- install firebase to fetch data from firebase
- - npm install @react-native-firebase/app @react-native-firebase/firestore

# errors
- For 404 error - Wrong base url.
- if docker images are not visible in docker tab
       - https://stackoverflow.com/questions/69530014/failed-to-connect-is-docker-running-vs-code




# VS code shortcut:

- toggle word wrap - (option + Z)
- convert cell to markdown - (Esc + M)
- convert cell to code - (Esc + Y)
- format json file - (Shift + option + F)




# My own thoughts
- Initially I started deploying an open source LLM model in my local machine.
- I dont remember the model name exactly but its fastchat model with 3b parameters.
- I have downloaded the model using huggingface library.
- The pipeline uses model(fastchat) and tokenizer(Autotokenizer) which is text2text-generation which can be viewed under model name in hugging face website.

- Later started to practice on prompt engineering by using the opensource LLama 8b model which is deployed on runpod.
- Main concept that I have learnt is RAG
        - I take content from 2 different sources (iphone, samsung).
        - enbeddings are gathered for that data and we perform consine similarity on the userpomrpt and the data provided.
        - The array index for which we get the greateer value is the one that the LLM model outputs.
        - This is how it works internally in fectching the content for the userinput we give.

- then I moved to recommendation enginer
- took data from kaggle and loaded sales_receipt and product csv files.
- toook important feature from it and merged both the data on product_id.
- removed rows of unnecessary products (focussed on only coffee products)
- grouped by product and product category and listed the count. (This is the popularity recomendation)
- then grouped product and transaction band listed down the count.
- The above dataframe is widened using pivot_table and fill Nan with 0's and this is taken into Apriori.
- the also found the association rules.
- using both, the for each antecedent, the information(confidence, product category) of consequent is stored as json.

- firebase is a realtime database when I uploaded the content from the product folder. using firebase_uploader.ipynb
- made use of firebase-admin and google-cloud-storage library
- product details are pushed as collection to realtime database.
- images are stored in storage bucket in firebase
- Use Firebase for a real-time database because it provides a cloud-hosted NoSQL database that automatically synchronizes data across all connected clients in real-time, 

- embedding database(vector database) - pinecone.
- you are actually implementing the RAG concept here, the similar way you did for Iphone and samsung. You create the embeddings and store them in the pinecone.
- When you want to get results from pinecone, you give an embedding, it automatically performs the cosine similarity with the embeddings data that it already has and return the top_k data.

