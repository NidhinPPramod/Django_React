import "./App.css";
import Axios from "axios";
import { useEffect, useState } from "react";
import BasicCard from "./Cards"

function App() {
  const[data,setData]=useState([])
  useEffect(() => {
    Axios.get("http://localhost:8000").then((res) => setData(res.data));
  }, []);
  return <div className="App">
    {data.map((val)=>(
      <BasicCard name={val.name} age={val.age} city={val.city}/>
    ))}
  
  </div>;
}

export default App;
