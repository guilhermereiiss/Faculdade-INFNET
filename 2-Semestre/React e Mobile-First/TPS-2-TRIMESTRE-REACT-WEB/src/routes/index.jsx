// import {
//     createBrowserRouter,
//     RouterProvider,
// } from "react-router-dom";

// import Home from "../views/Home"
// import SigIn from "../views/SigIn";
// import SingUp from "../views/SingUp";
// import Form from "../views/Form";
// import Settings from "../views/Settings";

// const router = createBrowserRouter([
//     {
//         path: "/TP/",
//         element: <Home/>,
//     },
//     {
//         path: "/TP/Form",
//         element: <Form/>,
//     },
//     {
//         path: "/TP/SigIn",
//         element: <SigIn/>,
//     },
//     {
//         path: "/TP/SingUp",
//         element: <SingUp/>,
//     },
//     {
//         path: "/TP/Settings",
//         element: <Settings/>,
//     },
// ]);

// const RouterApp = () =>{


    
//     return(
//         <div>
//             <RouterProvider router={router} />
//         </div>
//     )
// }


// export default RouterApp;

import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom";
// import { AuthProvider } from "./AuthContext"; 
import Home from "../views/Home";
import Dashboard from "../views/Dashboard";
import SignIn from "../views/SigIn";
import SignUp from "../views/SingUp";
import Form from "../views/Form";
import Settings from "../views/Settings";
// import PrivateRoute from "./PrivateRoute"; 

import Protected from "./protected";
import { handleVerificationProtected, isAuthenticated, signIn } from "../services/authentication";

const router = createBrowserRouter(
    createRoutesFromElements(
        <Route path="/TP/">
            <Route element={<Protected/>}>
                <Route index element={<Home />} loader={() => handleVerificationProtected()}/>
                <Route path="dashboard" element={<Dashboard />} loader={() => handleVerificationProtected()}/>
                <Route path="new/:type" element={<Form />} loader={() => handleVerificationProtected()}/>
                <Route path=":type/:id" element={<Form />} loader={() => handleVerificationProtected()}/>
            </Route>
            <Route path="signin" element={<SignIn />} loader={() => isAuthenticated()}/>
            <Route path="signup" element={<SignUp />} loader={() => isAuthenticated()}/>
        </Route>
    )
);

const Index = () => {
    return <RouterProvider router={router} />
}

export default Index;
