// Example for testing ks2d1s
//
// davekw7x
//
#include "../code/nr3.h"
#include "../code/gamma.h"
#include "../code/sort.h"
#include "../code/moment.h"
#include "../code/incgammabeta.h"
#include "../code/erf.h"
#include "../code/stattests.h"
#include "../code/quadvl.h"
#include "../code/ksdist.h"
#include "../code/kstests_2d.h"
#include "../code/ran.h"

int main() 
{
    Int num_points, num_trials;
    Doub factor;

    // For debugging, you might want to use the same
    // seed each time so that you can evaluate the
    // effects of program changes
    Int seed = 12345678;

    //
    // For repeated testing, you might want to use
    // a different seed each time
    //
    //Int seed = time(0);
    Ran ran(seed);

    cout << "Enter the number of points (Must be a greater than 2): ";
    //
    // Terminate the program if the user enters something non-numeric
    // or if the value is less than three
    //
    while ((cin >> num_points) && (num_points > 2)) {

        //
        // Low values of the factor makes the point distribution
        // be jointly uniform. As factor gets larger, the
        // distribution gets "less and less" jointly uniform
        //

        // Terminate the loop and exit the program if the user
        // makes a non-numeric entry, otherwise make sure an
        // appropriate value is entered, then proceed.
        //
        cout << "Enter the non-linearity factor (0.0 to 1.0)          : ";
        while ((cin >> factor) && ((factor < 0) || (factor > 1.0))) {

            if (factor < 0.0) {
                cout << "Factor can not be less than 0." << endl;
            }
            if (factor > 1.0) {
                cout << "Factor can not be greater than 1." << endl;
            }
            cout << endl;
            cout << "Enter the non-linearity factor (0.0 to 1.0)          : ";
        }
        if (!cin) {
            break;
        }

        //
        // Terminate the loop and exit the program if the user
        // makes a non-numeric entry, otherwise make sure an
        // appropriate value is entered, then proceed.
        //
        cout << "Enter the number of trials                           : ";
        while ((cin >> num_trials) && (num_trials <= 0)) {

            cout << "Must be a positive integer."
                 << endl << endl;
            cout << "Enter the number of trials                           : ";
        }
        if (!cin) {
            break;
        }

        cout << endl << endl
             << "The null hypothesis is that the distribution of the"
             << endl
             << "points (x,y) is jointly uniform for x in [-1,1] and"
             << endl
             << "and y in [-1,1]"
             << endl << endl
             << "If the probability number in the table is small, then"
             << endl
             << "we reject the null hypothesis, and we believe that the"
             << endl
             << "distribution is not jointly uniform in the given region."
             << endl << endl;

        cout << "                 Probability that D is greater"
             << endl
             << "K-S D value           than the K-S D value"
             << endl
             << "---------------------------------------------------"
             << endl;

        VecDoub x(num_points), y(num_points);
        for (Int i  = 0; i < num_trials; i++) {
            for (Int j = 0; j < num_points; j++) {

                Doub rand_temp = ran.doub();

                rand_temp = rand_temp * ((1.0 - factor) + rand_temp * factor);
                x[j] = 2.0 * rand_temp - 1.0;

                rand_temp = ran.doub();
                rand_temp = rand_temp * ((1.0 - factor) + rand_temp * factor);
                y[j] = 2.0 * rand_temp - 1.0;

            }

            Doub d, prob;
            ks2d1s(x, y, quadvl, d, prob);
            cout << fixed      << setprecision(6) << setw(9)  << d
                 << scientific << setprecision(2) << setw(24) << prob
                 << endl;
        }
        cout << endl << endl
             << "========================================================="
             << endl << endl;

        cout << "Enter the number of points (Must be a greater than 2): ";
    }
    if (cin) {
        cout << "Goodbye for now." << endl;
    }
    else {
        cout << "Invalid entry. Program is ending." << endl;
    }

    return 0;
}
