#include <mex.h>

/*
 * printarray.c
 * Prints the contents of an array. This is useful to find out the order of acces from C.
 */

void printarray(double *x, mwSize n)
{
    mexPrintf("The number of elements in the array is n=%d.\n\n", n);

    mexPrintf("array=[\n");
    for (mwSize i = 0; i < n; ++i)
        mexPrintf("\t%f,\n", x[i]);
    mexPrintf("]\n");
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    if (nrhs != 1)
        mexErrMsgIdAndTxt("printarray:nrhs", "One input required.");

    if (nlhs != 0)
        mexErrMsgIdAndTxt("printarray:nlhs", "No input required.");

    /* create pointer to the real data in the input vector */
    double* inArray = mxGetPr(prhs[0]);

    /* number of elements in the input array */
    mwSize n = mxGetNumberOfElements(prhs[0]);

    /* call the main routine */
    printarray(inArray, n);
}
