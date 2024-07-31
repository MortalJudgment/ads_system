import React, { useState, useEffect } from 'react';
import { fetchAds } from '../../services/api';
import './AdDisplay.css';

function AdDisplay({ userInterests }) {
  const [currentAd, setCurrentAd] = useState(null);

  useEffect(() => {
    const getAd = async () => {
      const ads = await fetchAds(userInterests);
      if (ads.length > 0) {
        setCurrentAd(ads[0]); // For simplicity, just showing the first ad
      }
    };
    getAd();
  }, [userInterests]);

  if (!currentAd) return null;

  return (
    <div className="ad-display">
      <h3>{currentAd.AdName}</h3>
      <p>{currentAd.AdDescription}</p>
      <a href={currentAd.AdURL} target="_blank" rel="noopener noreferrer">Learn More</a>
    </div>
  );
}

export default AdDisplay;