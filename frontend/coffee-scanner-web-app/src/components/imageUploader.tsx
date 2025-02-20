'use client';

import { useState } from "react";

export default function ImageUpload() {
    const [image, setImage] = useState<string | null>(null);
    const [file, setFile] = useState<File | null>(null);
    
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const selectedFile = event.target.files[0];
            setFile(selectedFile);
            setImage(URL.createObjectURL(selectedFile));
        }
    };

    const handleUpload = async () => {
        if (!file) return;
        const formData = new FormData();
        formData.append("image", file);
        
        try {
            const response = await fetch("http://127.0.0.1:8000/upload", {
                method: "POST",
                body: formData,
            });
            if (response.ok) {
                console.log("Upload successful");
            } else {
                console.error("Upload failed");
            }
        } catch (error) {
            console.error("Error uploading file", error);
        }
    };

    return (
            <div className="flex flex-col items-center justify-center w-full">
                {!image ? (
                <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                    <input type="file" accept="image/*" capture="environment" className="hidden" onChange={handleFileChange} />
                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                        </svg>
                        <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
                    </div>
                </label>
            ) : (
            <div className="mt-4">
                <img src={image} alt="Uploaded preview" className="w-full h-48 object-cover rounded-lg" />
                <div className="flex gap-4 mt-2">
                    <button onClick={() => { setImage(null); setFile(null); }} className="px-4 py-2 bg-gray-500 text-white rounded">Retake</button>
                    <button onClick={handleUpload} className="px-4 py-2 bg-blue-500 text-white rounded">Upload</button>
                </div>
            </div>
        )}
        </div>
    )
}
