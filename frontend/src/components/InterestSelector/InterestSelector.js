import React from 'react';
import './InterestSelector.css';

const interestOptions = ['Sports', 'Travel', 'Technology', 'Music', 'Food', 'Fashion'];

function InterestSelector({ interests, setInterests }) {
  const toggleInterest = (interest) => {
    if (interests.includes(interest)) {
      setInterests(interests.filter(i => i !== interest));
    } else {
      setInterests([...interests, interest]);
    }
  };

  return (
    <div className="interest-selector">
      <h3>Select your interests (at least 2):</h3>
      <div className="interest-options">
        {interestOptions.map(interest => (
          <button
            key={interest}
            className={interests.includes(interest) ? 'selected' : ''}
            onClick={() => toggleInterest(interest)}
          >
            {interest}
          </button>
        ))}
      </div>
    </div>
  );
}

export default InterestSelector;