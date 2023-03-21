import React, { useEffect, useState, useContext } from 'react'
import {AuthContext} from '../context/AuthContext.jsx'

const HomePage = () => {
  let [colors, setColor] = useState([])
  let {authTokens} = useContext(AuthContext)
  useEffect(()=>{
    getColor()
  }, [])
  let getColor = async()=>{
    let response = await fetch('http://localhost:8000/api/color/',{
    method : 'GET',
    headers : {
          'Content-Type' : 'application/json',
          'Authorization' :  'Bearer ' +  String(authTokens.access)
    }
    })
    let data = await response.json()
    console.log(data)
    setColor(data)
  }
  return (
    <div>You are logged in HomePage


    <ul>
      { colors.map(color=> (
        <li key={color.id}>
        {color.name}
        </li>
      )
      )}
    </ul>
    </div>


  )
}

export default HomePage
