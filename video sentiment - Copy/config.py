import os

class Config:
    # Directory to temporarily store uploaded videos
    UPLOAD_FOLDER = 'uploads'
    
    # Resend API Configuration
    # Replace 're_123456789...' with your actual Resend API Key
    RESEND_API_KEY = 're_cZ5QFqtr_5em5r38CubQLii9bBiTbXnD7'
    
    # Resend requires a verified domain or their onboarding email to send
    RESEND_SENDER = 'onboarding@resend.dev'                #ssl=Secure Sockets Layer.
    