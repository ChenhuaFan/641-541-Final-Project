import './App.css';
import Webcam from "react-webcam";
import axios from 'axios';
import { useState, useEffect, useRef, useMemo, useCallback } from 'react';

function App() {

  const [pred, setPred] = useState([]);
  const [image, setImage] = useState('');
  const [sentence, setSentence] = useState('');
  const [startInput, setStartInput] = useState(false);
  const screenshot = useRef('');
  const preCharRef = useRef({ 'pre': '', 'times': 0 });

  const videoConstraints = {
    width: 720,
    height: 720,
    facingMode: "user"
  };

  const getPred = useCallback(async (image) => {
    try {
      const res = await axios({
        method: 'post',
        url: '/api/predictions/CustomResNet18',
        headers: {
          "content-type": "application/json",
        },
        data: image,
      });
      // update word
      setPred(res.data)
    } catch (error) {
      console.error(error)
    }
  }, [])

  const currentChar = useMemo(() => {
    return Object.keys(pred)[0];
  }, [pred])

  useEffect(() => {
    if (image == null || !startInput) return;
    getPred(image)
    if (currentChar === preCharRef.current.pre) {
      preCharRef.current.times += 1
      if (preCharRef.current.times >= 4) {
        switch (preCharRef.current.pre) {
          case 'del':
            setSentence(sentence.substring(0, sentence.length - 1))
            break;
          case 'nothing':
            break;
          case 'space':
            setSentence(sentence + ' ')
            break;
          default:
            setSentence(sentence + currentChar)
            break;
        }
        preCharRef.current.times = 0
      }
    } else {
      preCharRef.current.pre = currentChar
      preCharRef.current.times = 0
    }
  }, [currentChar, getPred, image, sentence, startInput])

  useEffect(() => {
    function tick() {
      const img = screenshot.current();
      img && setImage(img.split(',')[1])
    }
    let id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  return (
    <div className="main">
      <div className="App">
        <Webcam
          className='web-cam'
          audio={false}
          height={300}
          screenshotFormat="image/jpeg"
          width={300}
          videoConstraints={videoConstraints}
        >
          {({ getScreenshot }) => {
            screenshot.current = getScreenshot
            return null
          }}
        </Webcam>
        <div className='pred'>
          {Object.keys(pred).map((k, i) => {
            const p = pred[k]
            return <p key={k}>{k}: <span>{p.toFixed(2)}</span></p>
          })}
        </div>
        <div className='current-pred'>{currentChar}</div>
      </div>
      <div className='playground'>
        <h2>🎮 Input sentence <button onClick={() => setStartInput(!startInput)}>{startInput ? 'Pause' : 'Start'}</button> <button onClick={() => setSentence('')}>Clear!</button></h2>
        <p>After 4 times same output, we may consider it's the target char.</p>

        <br />

        <p className='sentence'>{sentence}</p>
      </div>
    </div>
  );
}

export default App;
