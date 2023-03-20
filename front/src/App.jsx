import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'
import { AuthProvider } from './context/AuthContext.jsx'
import HomePage from './pages/HomePage.jsx'
import LoginPage from './pages/LoginPage'
import PrivateRouter from './utils/PrivateRouter.jsx'
import Header from './components/Header.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
    <AuthProvider>
     <Header />
     <Routes>
          <Route exact path="/" element={<PrivateRouter />}>
            <Route element={<HomePage />} path="/" exact />
          </Route>
          <Route element={<LoginPage />} path="/login" />
      </Routes>
    </AuthProvider>
    </div>
  )
}


export default App
