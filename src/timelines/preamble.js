import { prePracticeInstructions } from "../trials/instructions";
import welcome from "../trials/welcome";
import startCode from "../trials/startCode";
import { AT_HOME } from "../config/main";
import { practiceBlock1 } from "../config/practice";

console.log("at_home", AT_HOME);
console.log("env at home", process.env.REACT_APP_AT_HOME);
console.log("check this is running the correct branch in browser");
const preamble = {
  type: "html_keyboard_response",
  stimulus: "",
  timeline: AT_HOME
    ? [welcome, prePracticeInstructions(practiceBlock1)]
    : [startCode(), welcome, prePracticeInstructions(practiceBlock1)],
};

export default preamble;
