
import {createBrowserRouter,RouterProvider,Navigate,} from "react-router-dom";

import Home from "../pages/Home/Home";
import Favoritos from "../pages/Favoritos/Favoritos";
import NotFound from "../pages/notFound/notFound";
import Login from "../pages/Login";
import Start from "../pages/Start";
import Detalhes from "../pages/Detalhes/Detalhes";


const PrivateRoute = ({ element }) => {
    const isAuthenticated = localStorage.getItem('email') && localStorage.getItem('senha');
    return isAuthenticated ? element : <Navigate to="/MatchMovie/login" />;
};


const router = createBrowserRouter([
    {
        path: "/MatchMovie/",
        element: <Start />,
    },
    {
        path: "/MatchMovie/home",
        element: <Home />,
    },
    {
        path: "/MatchMovie/*",
        element: <NotFound />,
    },
    {
        path: "/MatchMovie/favoritos",
        element: <PrivateRoute element={<Favoritos />} />,
    },
    {
        path: "/MatchMovie/detalhes/:id",
        element: <Detalhes />,
    },
    {
        path: "/MatchMovie/login",
        element: <Login />,
    },
]);

const RouterApp = () => {
    const corSetada = localStorage?.getItem("@tema") ?? null;
    if (corSetada === 'escuro') {
        document.documentElement.setAttribute("data-tema", "escuro");
    } else if (corSetada === 'claro') {
        document.documentElement.setAttribute("data-tema", "claro");
    } else if (matchMedia('(prefers-color-scheme:dark)').matches) {
        document.documentElement.setAttribute("data-tema", "escuro");
    }

    return (
        <div>
            <RouterProvider router={router} />
        </div>
    );
};

export default RouterApp;
