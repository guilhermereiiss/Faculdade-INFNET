import { createBrowserRouter, RouterProvider, } from "react-router-dom";

import Home from './pages/Home/home.jsx'
import NotFound from './pages/not-found/notFound.jsx'
import Favoritos from './pages/Favoritos/Favoritos.jsx'
import Detalhes from './pages/Detalhes/detalhes.jsx'


const router = createBrowserRouter([
    {
        path: "/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/",
        element: <Home />
    },
    {
        path: "/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/*",
        element: <NotFound />
    },
    {
        path: "/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/favoritos",
        element: <Favoritos />
    },
    {
        path: "/AT_FUNDAMENTOS_REACT_GUILHERME_REIS/detalhes/:id",
        element: <Detalhes />
    },
]);


const App = () => {
    
        const corSetada = localStorage?.getItem("@tema") ?? null
        if (corSetada === 'escuro') {
            document.documentElement.setAttribute("data-tema", "escuro")
        } else if (corSetada === 'claro') {
            document.documentElement.setAttribute("data-tema", "claro")
        } else if (matchMedia('(prefers-color-scheme:dark)').matches) {
            console.log(matchMedia('(prefers-color-scheme:dark)'))
            document.documentElement.setAttribute("data-tema", "escuro");
        }
   

    return (
        <div>
            <RouterProvider router={router} />
        </div>
    )
}

export default App