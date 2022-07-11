import cv2
import qrcode
from pyzbar.pyzbar import decode
from barcode import EAN13
from barcode.writer import ImageWriter
import os



def readQR():
    # Take image location from user
    imageLocation = input("Enter Image Path: ")

    # Read the image
    img = cv2.imread(imageLocation)

    # Store the QR code reader in a variable
    qrCodeDetector = cv2.QRCodeDetector()

    # Decode the QR code
    try:
        decodedText, points, _ = qrCodeDetector.detectAndDecode(img)
        # Print Decoded text
        print("The text is:",decodedText)
    except:
        print("Enter valid Image Location!")
    
def makeQR():
    # Take input from user
    encodingText = input("Enter text to encode into QR: ")

    # Adjust QR Code Configuration
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Encode text into the QR Code
    qr.add_data(encodingText)
    qr.make(fit=True)

    # Set colour of the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Ask User to save or display
    saveOrNot = input("Save the image or Display the Image? (S/D): ").lower()
    # Save
    if saveOrNot == 's':
        name = input("Enter name to save: ")
        img.save(name+".png")
    # Display
    elif saveOrNot == 'd':
        img.show()
    # Save and Display
    elif saveOrNot == "sd":
        name = input("Enter name to save: ")
        img.save(name+".png")
        img.show()
    else:
        print("Error! Invalid Choice!")

def readBarcode():
    # Take image location from user
    imageLocation = input("Enter Image Path: ")

    # read the image in numpy array using cv2
    img = cv2.imread(imageLocation)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:       
            if barcode.data != "": 
            # Print the barcode data
                print("The data in barcode is:",str(barcode.data)[2:-1])

def makeBarcode():
    # Get 13 digit number from user
    number = input("Enter a 13 digit number: ")
    if len(number) != 13:
        print("Error! Length should be 13!")
    else:
        # Now, let's create an object of EAN13
        # class and pass the number
        my_code = EAN13(number, writer=ImageWriter())

        # Ask User to save or display
        saveOrNot = input("Save the image or Display the Image? (S/SD): ").lower()
        # Save
        if saveOrNot == 's':
            name = input("Enter name to save: ")
            my_code.save(name)
        # Display
        elif saveOrNot == 'd':
            # Save the image
            my_code.save(number)
            myCode = cv2.imread(number+".png")
            cv2.imshow(number,myCode)
            cv2.waitKey(0)

            # Delete the image
            os.remove(number+".png")
        # Save and Display
        elif saveOrNot == "sd":
            name = input("Enter name to save: ")
            my_code.save(name)
            myCode = cv2.imread(name+".png")
            cv2.imshow(name,myCode)
            cv2.waitKey(0)

        else:
            print("Error! Invalid Choice!")

userChoice = input("Select an option:\n1) Read\n2) Make\n")
if userChoice == '1':
    userChoice = input("1) QR\n2) Barcode\nWhat to Read : ")
    if userChoice == '1':
        readQR()
    elif userChoice == '2':
        readBarcode()
    else:
        print("Enter a valid choice!")
elif userChoice == '2':
    userChoice = input("1) QR\n2) Barcode\nWhat to Read : ")
    if userChoice == '1':
        makeQR()
    elif userChoice == '2':
        makeBarcode()
    else:
        print("Enter a valid choice!")
else:
    print("Enter a valid option!")