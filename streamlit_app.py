import React, { useState, useEffect, useRef } from 'react';
import {
SCENE_OPTIONS, CITY_OPTIONS, OUTFIT_OPTIONS, DESIGNER_OPTIONS,
SHOE_OPTIONS, ACCESSORY_OPTIONS, HAIR_OPTIONS, MAKEUP_OPTIONS,
NAIL_OPTIONS, POSE_OPTIONS, LIGHTING_OPTIONS, ASPECT_RATIO_OPTIONS,
IMAGE_COUNT_OPTIONS, DEFAULT_SETTINGS
} from './constants';
import { StudioSettings, GeneratedImage, Folder } from './types';
import { generatePhotos } from './services/geminiService';
import {
getGallery, saveImageToGallery, deleteImageFromGallery,
getFolders, createFolder, updateImageFolder
} from './utils/storage';
type Page = 'home' | 'studio' | 'gallery';
export default function App() {
const [currentPage, setCurrentPage] = useState<Page>('home');
const [identityImage, setIdentityImage] = useState<string | null>(null);
const [settings, setSettings] = useState<StudioSettings>(DEFAULT_SETTINGS);
const [isGenerating, setIsGenerating] = useState(false);
const [progress, setProgress] = useState({ current: 0, total: 0 });
const [sessionResults, setSessionResults] = useState<GeneratedImage[]>([]);
const [gallery, setGallery] = useState<GeneratedImage[]>([]);
const [folders, setFolders] = useState<Folder[]>([]);
const [showFolderModal, setShowFolderModal] = useState<{show: boolean, imageId: string | null}>({show: false, imageId: null});
const fileInputRef = useRef<HTMLInputElement>(null);
useEffect(() => {
setGallery(getGallery());
setFolders(getFolders());
}, [currentPage]);
const handleIdentityUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
const file = e.target.files?.[0];
if (file) {
const reader = new FileReader();
reader.onloadend = () => setIdentityImage(reader.result as string);
reader.readAsDataURL(file);
}
};
const handleGenerate = async () => {
if (!identityImage) {
alert("Please upload an identity photo first.");
return;
}
code
Code
setIsGenerating(true);
setSessionResults([]);

try {
  const urls = await generatePhotos(identityImage, settings, (current, total) => {
    setProgress({ current, total });
  });


  const newImages: GeneratedImage[] = urls.map(url => ({
    id: Math.random().toString(36).substr(2, 9),
    url,
    timestamp: Date.now(),
    settings: { ...settings },
    folder: 'default'
  }));


  setSessionResults(newImages);
  newImages.forEach(img => saveImageToGallery(img));
  setGallery(getGallery());
} catch (error) {
  console.error(error);
  alert("Failed to generate photos. Please check your settings and try again.");
} finally {
  setIsGenerating(false);
  setProgress({ current: 0, total: 0 });
}
};
const downloadImage = (url: string, id: string) => {
const link = document.createElement('a');
link.href = url;
link.download = radiant image ai-${id}.png;
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
};
const handleDelete = (id: string) => {
if (confirm("Are you sure you want to delete this photo?")) {
deleteImageFromGallery(id);
setGallery(getGallery());
setSessionResults(prev => prev.filter(img => img.id !== id));
}
};
const renderNav = () => (
<nav className="flex items-center justify-between px-8 py-6 border-b border-gray-800 bg-[#0B1020] sticky top-0 z-50">
<div className="flex items-center gap-2 cursor-pointer" onClick={() => setCurrentPage('home')}>
<div className="w-8 h-8 gold-bg rounded-sm flex items-center justify-center">
<span className="text-black font-bold text-xs">TS</span>
</div>
st.header("L Owens Systems")
</div>
<div className="flex gap-8 items-center uppercase tracking-tighter text-xs font-semibold">
<button onClick={() => setCurrentPage('home')} className={${currentPage === 'home' ? 'gold-text' : 'text-gray-400'} hover:gold-text transition-colors}>Home</button>
<button onClick={() => setCurrentPage('studio')} className={${currentPage === 'studio' ? 'gold-text' : 'text-gray-400'} hover:gold-text transition-colors}>Studio</button>
<button onClick={() => setCurrentPage('gallery')} className={${currentPage === 'gallery' ? 'gold-text' : 'text-gray-400'} hover:gold-text transition-colors}>Saved Gallery</button>
<button onClick={() => setCurrentPage('studio')} className="gold-bg text-black px-6 py-2 rounded-sm hover:opacity-90 transition-opacity">Launch Studio</button>
</div>
</nav>
);
const renderHome = () => (
<div className="min-h-screen">
{/* Hero Section */}
<section className="relative h-[80vh] flex flex-col items-center justify-center text-center px-4 overflow-hidden">
<div className="absolute inset-0 z-0 opacity-20">
<div className="absolute inset-0 bg-gradient-to-b from-[#0B1020] via-transparent to-[#0B1020]"></div>
<img
src="https://images.unsplash.com/photo-1539109132304-39155029cb40?auto=format&fit=crop&q=80&w=2000"
className="w-full h-full object-cover grayscale"
alt="luxury background"
/>
</div>
<div className="relative z-10 max-w-4xl">
<h2 className="text-6xl md:text-8xl font-serif italic mb-4 leading-tight">Build the vision. <br/> <span className="gold-text not-italic uppercase tracking-widest text-4xl md:text-6xl">Then wear it.</span></h2>
<p className="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto mb-10 font-light">
Realistic AI photos that look like you actually booked the shoot. Premium, high-end, and perfectly consistent.
</p>
<div className="flex flex-col md:flex-row gap-4 justify-center">
<button
onClick={() => setCurrentPage('studio')}
className="gold-bg text-black px-12 py-4 text-sm font-bold uppercase tracking-widest hover:scale-105 transition-transform"
>
Start Creating
</button>
<button
onClick={() => setCurrentPage('gallery')}
className="border border-white text-white px-12 py-4 text-sm font-bold uppercase tracking-widest hover:bg-white hover:text-black transition-all"
>
View Saved Photos
</button>
</div>
</div>
</section>
code
Code
{/* Motivation Grid */}
  <section className="py-24 px-8 max-w-7xl mx-auto">
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      {[
        { title: "No more fake-looking AI.", desc: "Pore-level detail and professional lighting." },
        { title: "No more inconsistent faces.", desc: "Identity Lock ensures it's always you." },
        { title: "No more wasted prompts.", desc: "Drop-down styling system for precision." },
        { title: "Building assets, not pictures.", desc: "Editorial quality ready for social & web." }
      ].map((item, i) => (
        <div key={i} className="p-8 border border-gray-800 hover:border-gold-500 transition-colors group">
          <div className="text-gold-500 mb-4 font-serif text-2xl italic">0{i+1}</div>
          <h3 className="text-xl font-bold mb-2 gold-text">{item.title}</h3>
          <p className="text-gray-400 text-sm leading-relaxed">{item.desc}</p>
        </div>
      ))}
    </div>
  </section>
</div>
);
const renderStudio = () => (
<div className="p-8 max-w-[1600px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12">
{/* Left Column: Form */}
<div className="lg:col-span-5 space-y-8 h-[calc(100vh-160px)] overflow-y-auto pr-4 custom-scrollbar">
<section>
<h3 className="text-xs font-bold uppercase tracking-widest gold-text mb-4 border-b border-gray-800 pb-2">01. Identity Lock</h3>
<div
onClick={() => fileInputRef.current?.click()}
className={border-2 border-dashed ${identityImage ? 'gold-border' : 'border-gray-700'} rounded-sm p-8 text-center cursor-pointer hover:border-gold-500 transition-all group}
>
{identityImage ? (
<div className="relative inline-block">
<img src={identityImage} className="h-48 w-48 object-cover rounded-sm mb-4 premium-shadow" alt="Identity" />
<div className="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
<span className="text-xs font-bold uppercase">Change Identity</span>
</div>
</div>
) : (
<div className="py-8">
<i className="fas fa-user-plus text-3xl mb-4 gold-text"></i>
<p className="text-sm font-semibold mb-1">Upload AI Twin / Influencer Identity</p>
<p className="text-xs text-gray-500">Forward facing, clear lighting, no accessories</p>
</div>
)}
<input type="file" ref={fileInputRef} onChange={handleIdentityUpload} className="hidden" accept="image/*" />
</div>
</section>
code
Code
<section className="space-y-6">
      <h3 className="text-xs font-bold uppercase tracking-widest gold-text mb-4 border-b border-gray-800 pb-2">02. Style & Concept</h3>
     
      <div className="grid grid-cols-2 gap-4">
        <div className="space-y-2">
          <label className="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Generation Mode</label>
          <select
            value={settings.appMode}
            onChange={(e) => setSettings({...settings, appMode: e.target.value as any})}
            className="w-full bg-[#161C2E] border border-gray-800 p-3 text-xs focus:gold-border outline-none"
          >
            <option>Baddie Luxury (styled)</option>
            <option>Designer Editorial (high fashion)</option>
            <option>Freestyle (you type the vibe)</option>
          </select>
        </div>
        <div className="space-y-2">
          <label className="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Image Count</label>
          <select
            value={settings.imageCount}
            onChange={(e) => setSettings({...settings, imageCount: e.target.value})}
            className="w-full bg-[#161C2E] border border-gray-800 p-3 text-xs focus:gold-border outline-none"
          >
            {IMAGE_COUNT_OPTIONS.map(opt => <option key={opt}>{opt}</option>)}
          </select>
        </div>
      </div>


      {settings.appMode !== 'Freestyle (you type the vibe)' ? (
        <div className="grid grid-cols-2 gap-4">
          {[
            { label: "Scene", key: "scene", options: SCENE_OPTIONS },
            { label: "City Vibe", key: "city", options: CITY_OPTIONS },
            { label: "Outfit Category", key: "outfitCategory", options: OUTFIT_OPTIONS },
            { label: "Designer", key: "designer", options: DESIGNER_OPTIONS },
            { label: "Shoes", key: "shoes", options: SHOE_OPTIONS },
            { label: "Accessories", key: "accessories", options: ACCESSORY_OPTIONS },
            { label: "Hair", key: "hair", options: HAIR_OPTIONS },
            { label: "Makeup", key: "makeup", options: MAKEUP_OPTIONS },
            { label: "Nails", key: "nails", options: NAIL_OPTIONS },
            { label: "Pose", key: "pose", options: POSE_OPTIONS },
            { label: "Lighting", key: "lighting", options: LIGHTING_OPTIONS },
            { label: "Aspect Ratio", key: "aspectRatio", options: ASPECT_RATIO_OPTIONS }
          ].map((field) => (
            <div key={field.key} className="space-y-2">
              <label className="text-[10px] uppercase tracking-wider text-gray-500 font-bold">{field.label}</label>
              <select
                value={settings[field.key as keyof StudioSettings] as string}
                onChange={(e) => setSettings({...settings, [field.key]: e.target.value})}
                className="w-full bg-[#161C2E] border border-gray-800 p-3 text-xs focus:gold-border outline-none"
              >
                {field.options.map(opt => <option key={opt}>{opt}</option>)}
              </select>
            </div>
          ))}
        </div>
      ) : (
        <div className="space-y-2">
          <label className="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Freestyle Prompt</label>
          <textarea
            value={settings.freestylePrompt}
            onChange={(e) => setSettings({...settings, freestylePrompt: e.target.value})}
            placeholder="Describe the exact photo you want. Keep it short and specific."
            className="w-full h-32 bg-[#161C2E] border border-gray-800 p-4 text-xs focus:gold-border outline-none resize-none"
          />
        </div>
      )}


      <div className="space-y-2">
        <label className="text-[10px] uppercase tracking-wider text-gray-500 font-bold">Custom Notes (Optional)</label>
        <textarea
          value={settings.customNotes}
          onChange={(e) => setSettings({...settings, customNotes: e.target.value})}
          placeholder="Add specific details for 'Other' selections..."
          className="w-full h-20 bg-[#161C2E] border border-gray-800 p-4 text-xs focus:gold-border outline-none resize-none"
        />
      </div>


      <button
        disabled={isGenerating || !identityImage}
        onClick={handleGenerate}
        className={`w-full py-4 uppercase tracking-widest text-sm font-bold flex items-center justify-center gap-3 transition-all ${isGenerating ? 'bg-gray-700 text-gray-400 cursor-not-allowed' : 'gold-bg text-black hover:scale-[1.01]'}`}
      >
        {isGenerating ? (
          <>
            <i className="fas fa-spinner fa-spin"></i>
            Rendering Your Shoot ({progress.current}/{progress.total})...
          </>
        ) : (
          <>
            <i className="fas fa-camera"></i>
            Generate Photos
          </>
        )}
      </button>
     
      {!identityImage && <p className="text-[10px] text-center text-red-400 uppercase tracking-widest font-bold">Upload identity photo to enable generation</p>}
    </section>
  </div>


  {/* Right Column: Results */}
  <div className="lg:col-span-7 bg-[#080C18] border border-gray-800 rounded-sm p-6 relative overflow-hidden min-h-[600px]">
    <h3 className="text-xs font-bold uppercase tracking-widest gold-text mb-6 flex justify-between items-center">
      <span>Results Preview</span>
      {sessionResults.length > 0 && <span className="text-gray-500 font-normal">{sessionResults.length} Images Generated</span>}
    </h3>


    {isGenerating && sessionResults.length === 0 ? (
      <div className="flex flex-col items-center justify-center h-[500px] text-center">
        <div className="w-16 h-1 gold-bg mb-4 overflow-hidden relative">
          <div className="absolute inset-0 bg-white animate-[shimmer_1s_infinite]"></div>
        </div>
        <p className="font-serif italic text-2xl mb-2">Rendering luxury...</p>
        <p className="text-xs text-gray-500 uppercase tracking-widest">Processing frame {progress.current} of {progress.total}</p>
      </div>
    ) : sessionResults.length > 0 ? (
      <div className="grid grid-cols-2 gap-4">
        {sessionResults.map((img) => (
          <div key={img.id} className="group relative aspect-[4/5] bg-black overflow-hidden premium-shadow border border-gray-800">
            <img src={img.url} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Generated" />
            <div className="absolute inset-0 bg-black bg-opacity-60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center gap-4">
              <div className="flex gap-2">
                <button
                  onClick={() => downloadImage(img.url, img.id)}
                  className="w-10 h-10 bg-white text-black flex items-center justify-center rounded-full hover:bg-gold-500 hover:text-white transition-colors"
                >
                  <i className="fas fa-download"></i>
                </button>
                <button
                  onClick={() => setShowFolderModal({show: true, imageId: img.id})}
                  className="w-10 h-10 bg-white text-black flex items-center justify-center rounded-full hover:bg-gold-500 hover:text-white transition-colors"
                >
                  <i className="fas fa-folder-plus"></i>
                </button>
                <button
                  onClick={() => handleDelete(img.id)}
                  className="w-10 h-10 bg-white text-black flex items-center justify-center rounded-full hover:bg-red-500 hover:text-white transition-colors"
                >
                  <i className="fas fa-trash"></i>
                </button>
              </div>
              <span className="text-[10px] font-bold uppercase tracking-tighter">Ultra-Real Export</span>
            </div>
          </div>
        ))}
      </div>
    ) : (
      <div className="flex flex-col items-center justify-center h-[500px] text-gray-600">
        <i className="fas fa-images text-5xl mb-6 opacity-20"></i>
        <p className="font-serif text-xl italic mb-2">Your shoot results will appear here</p>
        st.write(Studio Idle - Ready for command")
      </div>
    )}
  </div>
</div>
);
const renderGallery = () => {
const groupedGallery = folders.map(folder => ({
...folder,
images: gallery.filter(img => img.folder === folder.id || (!img.folder && folder.id === 'default'))
}));
code
Code
return (
  <div className="p-8 max-w-7xl mx-auto space-y-12">
    <header className="flex justify-between items-end border-b border-gray-800 pb-8">
      <div>
        <h2 className="text-4xl font-serif italic mb-2">Saved Gallery</h2>
        <p className="text-xs uppercase tracking-[0.3em] text-gray-500">The Permanent Collection</p>
      </div>
      <button
        onClick={() => {
          const name = prompt("Folder Name:");
          if (name) {
            createFolder(name);
            setFolders(getFolders());
          }
        }}
        className="border border-gold-500 gold-text text-[10px] font-bold px-6 py-2 uppercase tracking-widest hover:gold-bg hover:text-black transition-all"
      >
        Create New Folder
      </button>
    </header>


    {gallery.length === 0 ? (
      <div className="text-center py-32 border border-dashed border-gray-800">
        <p className="font-serif italic text-2xl text-gray-500 mb-4">Gallery is empty</p>
        <button onClick={() => setCurrentPage('studio')} className="gold-text uppercase text-xs font-bold tracking-widest">Start your first shoot</button>
      </div>
    ) : (
      <div className="space-y-16">
        {groupedGallery.map(group => group.images.length > 0 && (
          <section key={group.id} className="space-y-6">
            <div className="flex items-center gap-4">
              <h3 className="text-sm font-bold uppercase tracking-widest gold-text">{group.name}</h3>
              <div className="h-px flex-1 bg-gray-800"></div>
              <span className="text-[10px] text-gray-500 font-mono">{group.images.length} UNITS</span>
            </div>
            <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
              {group.images.map(img => (
                <div key={img.id} className="group relative aspect-[4/5] border border-gray-900 overflow-hidden">
                  <img src={img.url} className="w-full h-full object-cover transition-transform group-hover:scale-105" alt="Saved" />
                  <div className="absolute inset-0 bg-black bg-opacity-80 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center gap-2 p-2">
                     <div className="flex gap-1 flex-wrap justify-center">
                        <button onClick={() => downloadImage(img.url, img.id)} className="w-8 h-8 bg-white text-black text-xs flex items-center justify-center rounded-full"><i className="fas fa-download"></i></button>
                        <button onClick={() => setShowFolderModal({show: true, imageId: img.id})} className="w-8 h-8 bg-white text-black text-xs flex items-center justify-center rounded-full"><i className="fas fa-folder"></i></button>
                        <button onClick={() => handleDelete(img.id)} className="w-8 h-8 bg-red-500 text-white text-xs flex items-center justify-center rounded-full"><i className="fas fa-trash"></i></button>
                     </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>
    )}
  </div>
);
};
return (
<div className="min-h-screen pb-20">
{renderNav()}
code
Code
<main>
    {currentPage === 'home' && renderHome()}
    {currentPage === 'studio' && renderStudio()}
    {currentPage === 'gallery' && renderGallery()}
  </main>


  {/* Folder Modal */}
  {showFolderModal.show && (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black bg-opacity-90 p-4">
      <div className="bg-[#161C2E] border border-gold-500 p-8 max-w-md w-full premium-shadow">
        <h4 className="text-xl font-serif italic gold-text mb-6">Move to Collection</h4>
        <div className="space-y-2 mb-8">
          {folders.map(f => (
            <button
              key={f.id}
              onClick={() => {
                if (showFolderModal.imageId) {
                  updateImageFolder(showFolderModal.imageId, f.id);
                  setGallery(getGallery());
                  setShowFolderModal({show: false, imageId: null});
                }
              }}
              className="w-full text-left p-4 border border-gray-800 hover:border-gold-500 text-xs font-bold uppercase tracking-widest transition-colors flex justify-between items-center"
            >
              {f.name}
              <i className="fas fa-chevron-right opacity-30"></i>
            </button>
          ))}
        </div>
        <button
          onClick={() => setShowFolderModal({show: false, imageId: null})}
          className="w-full text-gray-500 text-[10px] uppercase font-bold tracking-widest hover:text-white"
        >
          Cancel
        </button>
      </div>
    </div>
  )}


  {/* Footer Branding */}
  <footer className="fixed bottom-0 left-0 right-0 py-4 px-8 border-t border-gray-800 bg-[#0B1020] text-[10px] text-gray-600 flex justify-between items-center uppercase tracking-widest">
    <span>&copy; 2026 L Owens Rewired</span>
    <div className="flex gap-6">
      <span className="gold-text font-bold">Encrypted Production Environment</span>
      <span>Terms of High-End Service</span>
    </div>
  </footer>


  <style>{`
    @keyframes shimmer {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }
    .custom-scrollbar::-webkit-scrollbar {
      width: 4px;
    }
    .custom-scrollbar::-webkit-scrollbar-track {
      background: #0B1020;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
      background: #1e293b;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {
      background: #C6A85A;
    }
  `}</style>
</div>
);
}
