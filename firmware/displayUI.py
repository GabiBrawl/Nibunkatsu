
tft.setTextColor(0xFFFF);
tft.setTextSize(1);
tft.setFreeFont(&FreeSerifItalic9pt7b);
tft.drawString("Nib", 4, 0);
tft.drawLine(1, 14, 30, 14, 0xFFFF);
tft.setFreeFont();
tft.drawString("Base", 5, 17);
tft.drawString("Cuts", 5, 25);
tft.drawString("Plus", 5, 33);
tft.drawBitmap(2, 19, image_Layer_6_bits, 2, 3, 0xFFFF);
tft.drawLine(2, 42, 29, 42, 0xFFFF);
tft.drawBitmap(3, 113, image_check_bits, 12, 16, 0xFFFF);
tft.drawBitmap(19, 113, image_cross_small_bits, 10, 16, 0xFFFF);
tft.drawLine(2, 113, 29, 113, 0xFFFF);
tft.drawBitmap(1, 43, image_menu_arrow_up_left_bits, 4, 4, 0xFFFF);
tft.drawBitmap(27, 43, image_menu_arrow_up_right_bits, 4, 4, 0xFFFF);
tft.drawBitmap(1, 109, image_menu_arrow_down_left_bits, 4, 4, 0xFFFF);
tft.drawBitmap(27, 109, image_menu_arrow_down_right_bits, 4, 4, 0xFFFF);
tft.drawLine(1, 47, 1, 108, 0xFFFF);
tft.drawLine(30, 47, 30, 108, 0xFFFF);





// banner
tft.setTextColor(0xFFFF);
tft.setTextSize(1);
tft.setFreeFont(&FreeSerifItalic9pt7b);
tft.drawString("Nibunkatsu One", 8, 8);
