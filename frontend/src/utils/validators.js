export function validateEmail(email) {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
}

export const validateUsername = (username) => {
    return username.length >= 3;
};

export const validatePassword = (password) => {
    return password.length >= 6;
};
  // Add more validation functions as needed