 using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace mig_2
{
    public partial class Form1 : Form
    {
        List<Point> points = new List<Point>(); //создание списка из точек
        SolidBrush br = new SolidBrush(Color.White);
        bool draw = false;//режим рисования off
        bool rejim = true;//режим рисования или закраски
        int a1;
        int a2; //этим переменным присавивается значение первой точки с которой начали фигуру

        List<int> zakrasheno = new List<int>();

        Bitmap Bit = new Bitmap(300, 500);

        public Form1()
        {
            InitializeComponent();
        }

        

        

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e) //происходит, когда пользователь нажимает кнопку мыши на элементе
        {
            label1.Text = "Шанс: ";
            if (rejim == true)
            {
                draw = true;
                Graphics g = pictureBox1.CreateGraphics();
                g.Clear(Color.Pink);
                a1 = e.X;
                a2 = e.Y;
            }
            else
            {
                draw = true;
                Graphics g = pictureBox1.CreateGraphics();
                a1 = e.X;
                a2 = e.Y;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e) // событие когда курсор мыши ездит по пикчербоксу
        {
            if (rejim == true)
            {
                Graphics g = pictureBox1.CreateGraphics(); //создать график на пикчербоксе
                                                           //координаты первой точки
                int x1 = e.X;
                int x2 = e.Y;

                Pen pen = new Pen(br, 3);

                //рисование при зажатой левой кнопке мыши (рисуем палочки во все стороны, имитируя точку)
                if (draw == true)
                {
                    g.DrawLine(pen, x1, x2, e.X + 1, e.Y + 1);
                    g.DrawLine(pen, x1, x2, e.X - 1, e.Y - 1);
                    g.DrawLine(pen, x1, x2, e.X + 1, e.Y - 1);
                    g.DrawLine(pen, x1, x2, e.X - 1, e.Y + 1);
                    g.DrawEllipse(pen, new Rectangle(e.X, e.Y, 3, 3));
                    points.Add(e.Location);
                    zakrasheno.Add(1);
                }

            }
            else //закраска
            {
                Graphics g = pictureBox1.CreateGraphics(); //создать график на пикчербоксе
                                                           //координаты первой точки
                int x1 = e.X;
                int x2 = e.Y;

                Pen pen = new Pen(br, 18);

                if (draw == true)
                {
                    g.DrawLine(pen, x1, x2, e.X + 3, e.Y + 3);
                    g.DrawLine(pen, x1, x2, e.X - 3, e.Y - 3);
                    g.DrawLine(pen, x1, x2, e.X + 3, e.Y - 3);
                    g.DrawLine(pen, x1, x2, e.X - 3, e.Y + 3);
                    g.DrawEllipse(pen, new Rectangle(e.X, e.Y, 5, 5));
                    points.Add(e.Location);
                    for (int i = 0; i < 28; i++) //добавим 28 закрашенных точек
                    {
                        zakrasheno.Add(1);
                    }
                }
            }

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e) //отпустили мышь
        {
            if (rejim == true) //это если рисуем контур
            {
                Pen pen = new Pen(br, 4);
                draw = false;
                //приблизительно точки должны совпасть
                if (Math.Abs(a1 - e.X) < 5 && Math.Abs(a2 - e.Y) < 5)
                {
                    Graphics g = pictureBox1.CreateGraphics();
                    g.DrawLine(pen, a1, a2, e.X, e.Y); //дорисуем

                }
                else //иначе очистка
                {
                    Graphics g = pictureBox1.CreateGraphics();
                    g.Clear(Color.Pink);
                    points.Clear();
                }
            }
            else 
            {
                draw = false;
            }
        }

        private void button1_Click(object sender, EventArgs e) //переход в режим закраски
        {
            rejim = false;
        }

        private void button3_Click(object sender, EventArgs e) //переход в режим контуров
        {
            rejim = true;
            draw = false;
        }

        private void button2_Click(object sender, EventArgs e) //очистка
        {
            Graphics g = pictureBox1.CreateGraphics();
            g.Clear(Color.Pink);
            points.Clear();
            zakrasheno.Clear();
            label1.Text = "Шанс: ";

        }

        private void button4_Click(object sender, EventArgs e) //подсчёт шанса
        {
            double d = Convert.ToDouble(zakrasheno.Count) / 150000;
            label1.Text = "Шанс примерно " + Math.Round(Convert.ToDouble(d*100))+" %";
        }
    }
}
