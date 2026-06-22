import Header from './header.jsx'
import ChatArea from './ChatArea.jsx'
import InputArea from './InputArea.jsx'
import './App.css'

function App(){
    return <div className="main-container"> 
        <Header/>
        <ChatArea/>
        <InputArea/>
        </div>
}

export default App