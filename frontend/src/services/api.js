const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export async function fetchAds(interests) {
  try {
    const response = await fetch(`${API_BASE_URL}/ads?interests=${interests.join(',')}`);
    if (!response.ok) throw new Error('Failed to fetch ads');
    return await response.json();
  } catch (error) {
    console.error('Error fetching ads:', error);
    return [];
  }
}

// Add more API functions as needed