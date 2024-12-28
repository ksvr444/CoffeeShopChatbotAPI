import { Stack } from "expo-router";
import "../global.css";
import { useFonts } from "expo-font";

export default function RootLayout() {
  const[fontsLoaded] = useFonts(
    {
      "Sora-Regular": require("../assets/fonts/Sora-Regular.ttf"),
      "Sora-SemiBold": require("../assets/fonts/Sora-SemiBold.ttf"),
      "Sora-Bold": require("../assets/fonts/Sora-Bold.ttf")
    }
  )
  return (
<Stack>
  <Stack.Screen name='index' options={{headerShown:false}} />
</Stack>
  );
}
