import { Navigate, Outlet } from 'react-router-dom'
import React, { useContext } from 'react'
import { AuthContext } from '../context/AuthContext.jsx'

const PrivateRouter = ({children, ...rest}) => {
  let  {user} = useContext(AuthContext)
  return user ? <Outlet /> : <Navigate to="/login" />;
}

export default PrivateRouter
