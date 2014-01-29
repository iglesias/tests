#include <mex.h>
#include <math.h>

/*
 * arraysqrt.c
 * Computes the element-wise square root of a vector.
 *
 * This is a mex-file for MATLAB.
 */

void arraysqrt(double *x, double *y, mwSize n)
{
    for (mwSize i = 0; i < n; ++i)
        y[i] = sqrt(x[i]);
}

/* The gateway function */
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    /* check for proper number of arguments and return values */
    if (nrhs != 1)
        mexErrMsgIdAndTxt("arraysqrt:nrhs", "Two inputs required.");
    
    if (nlhs != 1)
        mexErrMsgIdAndTxt("arraysqrt:nlhs", "One output required.");
    
    /* check for proper type of arugments */
    //TODO
    
    /* prepare input data */
    double *inVector;
    mwSize n;
    
    /* create pointer to the real data in the input vector */
    inVector = mxGetPr(prhs[0]);
    
    /* get the dimension of the input vector */
    n = mxGetN(prhs[0]);
    
    /* prepare output data */
    double *outVector;
    
    /* create the output vector */
    plhs[0] = mxCreateDoubleMatrix(1,n,mxREAL);
    
    /* get a pointer to the real data in the output vector */
    outVector = mxGetPr(plhs[0]);
    
    /* call the computation routine */
    arraysqrt(inVector, outVector, n);
}