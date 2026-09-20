# Capture the required application screenshot

The app launched successfully, but macOS rejected the automated capture with “could not create image from rect.” No application screenshot was fabricated.

1. Open a terminal in the repository, activate `.venv`, and run `python qr_generator.py`.
2. Enter `https://github.com/AshishM26/MSCS633_Assignment_2_QR_Gen` and click **Generate QR Code**.
3. Keep the complete URL, QR image, success message, and saved path visible.
4. On macOS press **Shift–Command–4**, then **Space**, and click the application window. On Windows use Snipping Tool; on Linux use the desktop Screenshot app.
5. Save/move the real capture to `screenshots/application_output.png`.
6. Open `report/MSCS633_Hands_On_Assignment_2_Report.docx` in Word. Replace the marked placeholder under section 3 using **Insert → Pictures**, keeping the image within the margins. Retain the figure caption and remove the pending-capture note.
7. Update `report/report_text.md` to replace its placeholder with `![Application output](../screenshots/application_output.png)` and remove the pending-capture statement. Update the README to reflect completion.
8. Save the report and commit the completed evidence:
   ```bash
   git add screenshots/application_output.png report/MSCS633_Hands_On_Assignment_2_Report.docx report/report_text.md README.md
   git commit -m "docs: add genuine application screenshot to report"
   git push origin main
   ```

Review the application and report yourself before submitting the Word document and repository URL to Blackboard. Phone scanning is optional additional human verification; no phone scan is claimed.
