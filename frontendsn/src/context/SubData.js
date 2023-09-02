import { createContext, useState} from "react";
export const SubContext = createContext({
   Detail : {
    name : '',
    email : '',
    phone : '',
   },
   setDetail : () => [{
    name : '',
    email : '',
    phone : '',
   }]
});
export const SubProvider = ({children}) => {
   const [Detail, setDetail] = useState({
    name : '',
    email : '',
    phone : '',
   });
   const value = {Detail, setDetail};
   
   return <SubContext.Provider value={value}>{children}</SubContext.Provider>
}