using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MatLog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            button2.Enabled = false; // изначально блокируем кнопки 2-6, чтобы без введения значений мы не могли нажать на кнопку получения ответа
            button3.Enabled = false; // для 3 кнопки
            button4.Enabled = false; // для 4 кнопки
            button5.Enabled = false; // для 5 кнопки
            button6.Enabled = false; // для 6 кнопки
            button7.Enabled = false; // для 7 кнопки
        }

        int a;// задаем глобальную переменную для а
        int b;// задаем глобальную переменную для b
        int ab; // задаем глобальную переменную для аb
        int abc; // задаем глобальную переменную для аbc
        int abcd; // задаем глобальную переменную для аbcd
        int abcdf = 0; // задаем глобальную переменную для аbcde

        private void button1_Click(object sender, EventArgs e) // метод для баловства, загрузил фотку для фона прикол хаха
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Image Files(*.BMP;*.JPG;*.GIF;*.PNG)|*.BMP;*JPG;*.GIF;*.PNG| All files (*.*)|*.*;"; // позволяем ввести в картинку прикол заданные типы файлов
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    pictureBox1.Image = new Bitmap(ofd.FileName); // позволяет внести саму картинку
                }
                catch
                {
                    MessageBox.Show("невозмжно открыть выбранный файл", "ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error); // выдает ошибку если была внесена вместо заданных типов файлов иной тип

                }
            }
        }



        private void textBox1_KeyPress(object sender, KeyPressEventArgs e) // метод для текстбокса 1  чтобы в окно можно было вводить либо 1 либо 0
        {


            char number = e.KeyChar;
            if ((e.KeyChar <= 47 || e.KeyChar >= 50) && number != 8)
            {
                e.Handled = true;
            }
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e) // метод для текстбокса 2 чтобы в окно можно было вводить либо 1 либо 0
        {
            char number = e.KeyChar;
            if ((e.KeyChar <= 47 || e.KeyChar >= 50) && number != 8)
            {
                e.Handled = true;
            }
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e) // метод для текстбокса 3 чтобы в окно можно было вводить либо 1 либо 0
        {
            char number = e.KeyChar;
            if ((e.KeyChar <= 47 || e.KeyChar >= 50) && number != 8)
            {
                e.Handled = true;
            }
        }

        private void textBox4_KeyPress(object sender, KeyPressEventArgs e) // метод для текстбокса 4 чтобы в окно можно было вводить либо 1 либо 0
        {
            char number = e.KeyChar;
            if ((e.KeyChar <= 47 || e.KeyChar >= 50) && number != 8)
            {
                e.Handled = true;
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e) // метод для текстбокса1 который не позволит нам ввести число наподобие 11 00 01 1110 и т.д.
        {
            //Проверка на пустоту, равность 0 и исключение чисел > 9
            if (textBox1.Text == ""
            || textBox1.Text.Count() > 1
            || textBox2.Text == ""
            || textBox2.Text.Count() > 1
            || textBox3.Text == ""
            || textBox3.Text.Count() > 1
            || textBox4.Text == ""
            || textBox4.Text.Count() > 1)
            {
                button2.Enabled = false;
                listBox1.Items.Clear();
                
            }
            //Проверка ввода чисел до 10, исключая 0
            else
            {
                listBox1.Items.Clear();
                listBox1.Items.Add("Ввод корректный.");
                button2.Enabled = true;
            }
            if ((textBox1.Text == "") || (textBox2.Text == "")|| (textBox1.Text.Count() > 1) || textBox2.Text.Count() > 1) // позволяет нажать на получение 1 ответа после введение P и Q
            {
                button3.Enabled = false;
                listBox1.Items.Clear();
                listBox1.Items.Add("Некорректный ввод.");
            }
            else
            {
                listBox1.Items.Clear();
                listBox1.Items.Add("Ввод корректный.");
                button3.Enabled = true;
                button7.Enabled = true;
            }
            if ((textBox1.Text == "") || (textBox2.Text == "") || (textBox3.Text == "") || (textBox1.Text.Count() > 1) || textBox2.Text.Count() > 1 || textBox3.Text.Count()>1) // позволяет нажать на получение 2 ответа после введения  R 
            {
                button4.Enabled = false;
                listBox1.Items.Clear();
                listBox1.Items.Add("Некорректный ввод.");
            }
            else
            {
                listBox1.Items.Clear();
                listBox1.Items.Add("Ввод корректный.");
                button4.Enabled = true;
            }
            if ((textBox1.Text == "") || (textBox2.Text == "") || (textBox3.Text == "") || (textBox4.Text=="") || (textBox1.Text.Count() > 1) || textBox2.Text.Count() > 1 || textBox3.Text.Count() > 1 || textBox4.Text.Count()>1) // позволяет нажать на получение ответа 3 и ответа 4 после введения S
            {
                button5.Enabled = false;
                button6.Enabled = false;
                listBox1.Items.Clear();
                listBox1.Items.Add("Некорректный ввод. ");
            }
            else
            {
                listBox1.Items.Clear();
                listBox1.Items.Add("Ввод корректный.");
                button5.Enabled = true;
                button6.Enabled = true;
            }



        }

        private void button3_Click(object sender, EventArgs e) // метод для пошагового вычисления (действие 1)
        {
             a = Convert.ToInt32(textBox1.Text);
             b = Convert.ToInt32(textBox2.Text);
             ab = 0;
            if ((a==0) && (b==0))
            {
                ab = 0;
                
            }
            if ((a == 0) && (b == 1))
            {
                ab = 1;

            }
            if ((a == 1) && (b == 0))
            {
                ab = 1;

            }
            if ((a == 1) && (b == 1))
            {
                ab = 1;

            }

            label7.Text = "После первого действия получим " + ab;
        }

        private void button4_Click(object sender, EventArgs e) //  метод для пошагового вычисления (действие 2)
        {
            abc = 0;
            int c = Convert.ToInt32(textBox3.Text);
            if ((ab == 0) && (c == 0))
            {
                abc = 0;

            }
            if ((ab == 0) && (c == 1))
            {
                abc = 1;

            }
            if ((ab == 1) && (c == 0))
            {
                abc = 1;

            }
            if ((ab == 1) && (c == 1))
            {
                abc = 1;

            }
            label8.Text = "После второго действия получим " + abc;
        }

        private void button5_Click(object sender, EventArgs e) // метод для пошагового вычисления (действие 3)
        {
            abcd = 0;
            int d = Convert.ToInt32(textBox4.Text);
            if ((abc == 0) && (d == 0))
            {
                abcd = 0;

            }
            if ((abc == 0) && (d == 1))
            {
                abcd = 0;

            }
            if ((abc == 1) && (d == 0))
            {
                abcd = 0;

            }
            if ((abc == 1) && (d == 1))
            {
                abcd = 1;

            }
            label9.Text = "После третьего действия получим " + abcd;

        }

        private void button6_Click(object sender, EventArgs e) // Сам метод для получения конечного ответа ( действие 4)
        {
            int f = 0;
            abcdf = 0;
            if (a == 0) // Условия для получения not P
            {
                f = 1;
            }
            if (a == 1)
            {
                f = 0;
            }

            if ((abcd == 0) && (f == 0)) // Логическое выражение для 4 действия
            {
                abcdf = 0;

            }
            if ((abcd == 0) && (f == 1))
            {
                abcdf = 0;

            }
            if ((abcd == 1) && (f == 0))
            {
                abcdf = 0;

            }
            if ((abcd == 1) && (f == 1))
            {
                abcdf = 1;

            }
            label10.Text = "После четвертого действия получим " + abcdf;
        }

        private void button2_Click(object sender, EventArgs e) // выводит полный ответ
        {

            label6.Text = "Ответ: " + abcdf;
        }

        private void button7_Click(object sender, EventArgs e) // максимально ленивый метод очистки ответов по кнопке
        {
            label6.Text = "Ответ: ";
            label7.Text = "После первого действия получим ";
            label8.Text = "После второго действия получим ";
            label9.Text = "После третьего действия получим ";
            label10.Text = "После четвертого действия получим ";
        }
    }
}
