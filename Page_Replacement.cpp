#include <iostream>
#include <vector>
using namespace std;

int n, nf;           // Number of pages and number of frames
vector<int> in(100); // Page reference sequence
vector<int> p(50);   // Frames
int hit = 0;
int pgfaultcnt = 0;

void getData()
{
    cout << "\nEnter length of page reference sequence: ";
    cin >> n;
    cout << "\nEnter the page reference sequence: ";
    for (int i = 0; i < n; i++)
        cin >> in[i];
    cout << "\nEnter no of frames: ";
    cin >> nf;
}

//resets frames to -1 and fault count = 0
void initialize()
{
    pgfaultcnt = 0;
    for (int i = 0; i < nf; i++)
        p[i] = -1; // Use -1 to represent empty frames
}

//is data already in frame
int isHit(int data)
{
    hit = 0;
    for (int j = 0; j < nf; j++)
    {
        if (p[j] == data)
        {
            hit = 1;
            break;
        }
    }
    return hit;
}

void dispPages()
{
    for (int k = 0; k < nf; k++)
    {
        if (p[k] != -1)
            cout << " " << p[k];
    }
}

void dispPgFaultCnt()
{
    cout << "\nTotal no of page faults: " << pgfaultcnt << endl;
}

//Swap the new page with the oldest one in a frame i.e which came at very first
void fifo()
{
    initialize();
    for (int i = 0; i < n; i++)
    {
        cout << "\nFor " << in[i] << " :";

        if (isHit(in[i]) == 0)
        {
            for (int k = 0; k < nf - 1; k++)
                p[k] = p[k + 1];

            p[nf - 1] = in[i];
            pgfaultcnt++;
            dispPages();
        }
        else
        {
            cout << " No page fault!";
        }
    }
    dispPgFaultCnt();
}

//Find a page that is not referenced in the future, or find a page that is refenced farthest in future
void optimal()
{
    initialize();
    vector<int> near(50);
    for (int i = 0; i < n; i++)
    {
        cout << "\nFor " << in[i] << " :";

        if (isHit(in[i]) == 0)
        {
            for (int j = 0; j < nf; j++)
            {
                int pg = p[j];
                int found = 0;
                for (int k = i; k < n; k++)
                {
                    if (pg == in[k])
                    {
                        near[j] = k;
                        found = 1;
                        break;
                    }
                }
                if (!found)
                    near[j] = 9999;
            }

            int max = -9999;
            int repindex;
            for (int j = 0; j < nf; j++)
            {
                if (near[j] > max)
                {
                    max = near[j];
                    repindex = j;
                }
            }
            p[repindex] = in[i];
            pgfaultcnt++;

            dispPages();
        }
        else
        {
            cout << " No page fault";
        }
    }
    dispPgFaultCnt();
}

//Replace a page that has not been used for the longest time i.e Least Recently Used
void lru()
{
    initialize();
    vector<int> least(50);
    for (int i = 0; i < n; i++)
    {
        cout << "\nFor " << in[i] << " :";

        if (isHit(in[i]) == 0)
        {
            for (int j = 0; j < nf; j++)
            {
                int pg = p[j];
                int found = 0;
                for (int k = i - 1; k >= 0; k--)
                {
                    if (pg == in[k])
                    {
                        least[j] = k;
                        found = 1;
                        break;
                    }
                }
                if (!found)
                    least[j] = -9999;
            }

            int min = 9999;
            int repindex;
            for (int j = 0; j < nf; j++)
            {
                if (least[j] < min)
                {
                    min = least[j];
                    repindex = j;
                }
            }
            p[repindex] = in[i];
            pgfaultcnt++;

            dispPages();
        }
        else
        {
            cout << " No page fault!";
        }
    }
    dispPgFaultCnt();
}

int main()
{
    int choice;
    while (true)
    {
        cout << "\nPage Replacement Algorithms\n1. Enter data\n2. FIFO\n3. Optimal\n4. LRU\n5. Exit\nEnter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            getData();
            break;
        case 2:
            fifo();
            break;
        case 3:
            optimal();
            break;
        case 4:
            lru();
            break;
        default:
            return 0;
        }
    }
}
