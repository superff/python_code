class Solution {
public:
     double findMedianSortedArrays(int A[], int m, int B[], int n) {
         int k=(m+n+1)/2-1;
         int s=findMedian(A,m,B,n,k);
         int t;
         int nA,nB;
         if((m+n)%2) return (double)s;
         else{
             nA = countSmaller(A,m,s+1);
             nB = countSmaller(B,n,s+1);
             if(nA+nB>(m+n)/2) return (double)s;
             nA = findNext(A,m,s);
             nB = findNext(B,n,s);
             if(nA<m){
                 t = A[nA];
                 if(nB<n) t=t<B[nB]?t:B[nB];
             }
             else{
                 t = B[nB];
             }
            return ((double)(s+t))/2.0;
                     }
     }
 
     int countSmaller(int A[],int m,int s){
         if(!m) return 0;
         if(A[m-1]<s) return m;
         if(s<=A[0]) return 0;
         int k=(m-1)/2;
         if(A[k]<s){
             A = A+k+1;
             m = m-k-1;
             return k+countSmaller(A,m,s)+1;
         }
         else{
             m = k;
             return countSmaller(A,m,s);
         }
     }
 
     int findNext(int A[],int m,int s){
         if(!m) return 0;
         if(A[m-1]<=s) return m;
         if(s<A[0]) return 0;
         int k=(m-1)/2;
         if(A[k]<=s){
             A = A+k+1;
             m = m-k-1;
             return k+findNext(A,m,s)+1;
         }
         else{
             m = k;
             return findNext(A,m,s);
         }
     }
 
     int findMedian(int A[],int m,int B[],int n,int k){
         if(!n) return A[k];
         if(!m) return B[k];
         if(!k) return A[0]>B[0]?B[0]:A[0];
         if(k==(m+n-1)) return A[m-1]<B[n-1]?B[n-1]:A[m-1];
         int kA = m*k/(m+n);
         int kB = n*k/(m+n);
         if(kA+kB!=k){
             if(m<n){
                 if(kA+1<m) kA++;
                 else kB++;          
             }
             else{
                 if(kB+1<n) kB++;
                 else kA++;
             }
         }
         if(A[kA]==B[kB]) return A[kA];
         else if(A[kA]<B[kB]){
             A = A+kA;
             m = m-kA;
             n = kB;
             k = k-kA;
         }
         else{
            m = kA;
             B = B+kB;
             n = n-kB;
             k = k-kB;
         }
         return findMedian(A,m,B,n,k);
     }
};