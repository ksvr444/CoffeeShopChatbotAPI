import { Text, View, SafeAreaView, ImageBackground } from "react-native";
import "../global.css";
export default function Index() {
  return (
    <View>
      <SafeAreaView className="w-full h-full">
        <ImageBackground className="w-full h-full items-center" source={require("../assets/images/index_bg_image.png")}> 
          <View className="flex h-[50%]"/>
          <View className="flex w-[80%]"/>
          <Text className="flex items-stretch bg-grey-lighter min-h-screen text-white text-3xl text-center mx-6 font-[Sora-Semibold]"> Fall in love with Coffee is Blissful Delight!</Text>

          
          <Text
            className="pt-3 text-[#A2A2A2] text-center font-[Sora-Regular] text-white">
            Welcome to out coffee shop corner
          </Text>

        </ImageBackground>
      </SafeAreaView>
    </View>
  );
}
