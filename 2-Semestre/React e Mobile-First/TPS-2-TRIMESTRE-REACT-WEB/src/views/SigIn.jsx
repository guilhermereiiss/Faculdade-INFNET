import { useTranslation } from "react-i18next";

const SigIn = () => {
  const { t } = useTranslation();

  return (
    <div>
        <h1>{t("Signin")}</h1>
        
    </div>
  )
}

export default SigIn

