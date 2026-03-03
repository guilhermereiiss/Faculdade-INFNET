import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const PrivateRoute = ({ element }) => {
    const { isAuthenticated } = useAuth();

    return isAuthenticated ? element : <Navigate to="/TP/SigIn" />;
};

export default PrivateRoute;
