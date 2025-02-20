//# frontend/pages/index.js (Next.js Frontend)
'use client';

import { useEffect, useState } from "react";

import ImageUpload from "@/components/imageUploader";

interface CoffeeData{
    name: string;
    origin: string;
}

// function GetApi(){
//     const file_data = readFileSync("./.venv/API.json", "utf-8");
//     return JSON.parse(file_data)["URL"]["local_network"];
// }

const API_BASE_URL = "http://192.168.1.4:8000/api/";

export default function Home() {
    // const [coffee, setCoffee] = useState<CoffeeData | null> (null);

    return(
    <div className="flex flex-col items-center justify-center min-h-screen bg-primary p-4 text-textColor">
        <h1 className="text-6xl font-bold mb-6 w-min">Coffee Logger</h1>
        <ImageUpload />

        {/* <h1 className="text-2xl font-bold">Coffee Logger</h1>
            {coffee ? (
                <p className="text-lg">{coffee.name} - {coffee.origin}</p>
            ) : (
                <p>Loading...</p>
            )} */}
    </div>

    
)


    // useEffect(() => {
    //     fetch(API_BASE_URL + "coffee")
    //         .then(res => res.json())
    //         .then((data: CoffeeData) => setCoffee(data))
    //         .catch(err => console.error("Failed to fetch coffee data:", err));
    // }, []);

    // return (
    //     <div className="flex flex-col items-center justify-center min-h-screen bg-primary text-textColor">
    //         <h1>Coffee Logger</h1>
    //         <div className="flex items-center justify-center w-full">
    //             <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
    //                 <div className="flex flex-col items-center justify-center pt-5 pb-6">
    //                     <svg className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
    //                         <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
    //                     </svg>
    //                     <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span> or drag and drop</p>
    //                     <p className="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
    //                 </div>
    //                 <input id="dropzone-file" type="file" className="hidden" />
    //             </label>
    //         </div> 


    //     </div>
    // );
}