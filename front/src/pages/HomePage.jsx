import React, { useEffect, useState, useContext } from 'react'
import {AuthContext} from '../context/AuthContext.jsx'

const HomePage = () => {
  let [colors, setColor] = useState([])
  let {authTokens, logoutUser} = useContext(AuthContext)
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


    if (response.status === 200){
      setColor(data)
    }else if( response.status === 401){
      logoutUser()
    }
     

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
