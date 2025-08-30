import { Outlet } from "react-router-dom";


export default function Layout(){
    return(
        <div 
            style={{
                backgroundColor: "#000", 
                height: '100vh', 
                width: '100vw'
            }}>
            <Outlet/>
        </div>
    )
}